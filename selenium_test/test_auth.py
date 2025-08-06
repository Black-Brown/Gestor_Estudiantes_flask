import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from conftest import TestConfig, take_screenshot

class TestAuthentication:
    """
    Pruebas para HU-001: Autenticación de Usuario
    """
    
    def test_successful_login(self, driver, wait):
        """
        Camino feliz: Login exitoso con credenciales correctas
        """
        try:
            # Ir a la página de login
            driver.get(f"{TestConfig.BASE_URL}/auth/login")
            
            # Verificar que estamos en la página de login
            assert "login" in driver.current_url
            
            # Llenar formulario de login
            username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
            password_field = driver.find_element(By.NAME, "password")
            
            username_field.send_keys(TestConfig.ADMIN_USERNAME)
            password_field.send_keys(TestConfig.ADMIN_PASSWORD)
            
            # Hacer click en el botón de login
            login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            login_button.click()
            
            # Esperar a que redirija al dashboard
            wait.until(EC.url_contains("/dashboard"))
            
            # Verificar que estamos en el dashboard
            assert "/dashboard" in driver.current_url
            
            # Verificar mensaje de éxito
            success_message = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "alert-success")))
            assert "Inicio de sesión exitoso" in success_message.text
            
            take_screenshot(driver, "test_successful_login")
            
        except Exception as e:
            take_screenshot(driver, "test_successful_login_error")
            raise e
    
    def test_failed_login_invalid_credentials(self, driver, wait):
        """
        Prueba negativa: Login fallido con credenciales incorrectas
        """
        try:
            # Ir a la página de login
            driver.get(f"{TestConfig.BASE_URL}/auth/login")
            
            # Llenar formulario con credenciales incorrectas
            username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
            password_field = driver.find_element(By.NAME, "password")
            
            username_field.send_keys("usuario_incorrecto")
            password_field.send_keys("password_incorrecto")
            
            # Hacer click en el botón de login
            login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            login_button.click()
            
            # Verificar que permanecemos en la página de login
            assert "/auth/login" in driver.current_url
            
            # Verificar mensaje de error
            error_message = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "alert-danger")))
            assert "Usuario o contraseña incorrectos" in error_message.text
            
            take_screenshot(driver, "test_failed_login_invalid_credentials")
            
        except Exception as e:
            take_screenshot(driver, "test_failed_login_invalid_credentials_error")
            raise e
    
    def test_failed_login_empty_fields(self, driver, wait):
        """
        Prueba de límites: Login con campos vacíos
        """
        try:
            # Ir a la página de login
            driver.get(f"{TestConfig.BASE_URL}/auth/login")
            
            # Llenar solo el campo de usuario y dejar la contraseña vacía
            username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
            username_field.send_keys("admin")
            
            # Hacer click en el botón de login
            login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            login_button.click()
            
            # Verificar que permanecemos en la página de login
            assert "/auth/login" in driver.current_url
            
            # Verificar mensaje de error
            error_message = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "alert-danger")))
            assert "Usuario o contraseña incorrectos" in error_message.text
            
            take_screenshot(driver, "test_failed_login_empty_fields")
            
        except Exception as e:
            take_screenshot(driver, "test_failed_login_empty_fields_error")
            raise e
    
    def test_logout(self, logged_in_driver, wait):
        """
        Camino feliz: Logout exitoso
        """
        try:
            # Ya estamos logueados gracias al fixture
            # Buscar y hacer click en el enlace de logout
            logout_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Cerrar Sesión")))
            logout_link.click()
            
            # Verificar que redirija al login
            wait.until(EC.url_contains("/auth/login"))
            assert "/auth/login" in logged_in_driver.current_url
            
            # Verificar mensaje de éxito
            success_message = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "alert-success")))
            assert "Has cerrado sesión exitosamente" in success_message.text
            
            take_screenshot(logged_in_driver, "test_logout")
            
        except Exception as e:
            take_screenshot(logged_in_driver, "test_logout_error")
            raise e 