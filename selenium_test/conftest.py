"""
Archivo de configuración de pytest que define las fixtures para Selenium
Este archivo es reconocido automáticamente por pytest
"""

import pytest
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestConfig:
    BASE_URL = "http://localhost:5000"
    ADMIN_USERNAME = "admin"
    ADMIN_PASSWORD = "admin123"
    IMPLICIT_WAIT = 10
    EXPLICIT_WAIT = 10

@pytest.fixture(scope="function")
def driver():
    # Fixture que configura y proporciona el driver de Chrome para cada prueba

    # Configurar opciones de Chrome
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--start-maximized")
    
    # Configurar el driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(TestConfig.IMPLICIT_WAIT)
    
    yield driver
    
    # Limpiar después de cada prueba
    driver.quit()

@pytest.fixture(scope="function")
def wait(driver):
    # Fixture que proporciona un WebDriverWait configurado

    return WebDriverWait(driver, TestConfig.EXPLICIT_WAIT)

@pytest.fixture(scope="function")
def logged_in_driver(driver, wait):
    # Fixture que proporciona un driver ya logueado en el sistema

    # Ir a la página de login
    driver.get(f"{TestConfig.BASE_URL}/auth/login")
    
    # Llenar formulario de login
    username_field = wait.until(EC.presence_of_element_located(("name", "username")))
    password_field = driver.find_element("name", "password")
    
    username_field.send_keys(TestConfig.ADMIN_USERNAME)
    password_field.send_keys(TestConfig.ADMIN_PASSWORD)
    
    # Hacer click en el botón de login
    login_button = driver.find_element("css selector", "button[type='submit']")
    login_button.click()
    
    # Esperar a que redirija al dashboard
    wait.until(EC.url_contains("/dashboard"))
    
    yield driver

def take_screenshot(driver, test_name):
    # Función para tomar capturas de pantalla automáticas
    
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    screenshot_dir = "screenshots"
    
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)
    
    filename = f"{screenshot_dir}/{test_name}_{timestamp}.png"
    driver.save_screenshot(filename)
    return filename 