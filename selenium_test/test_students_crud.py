import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from config_test import TestConfig, take_screenshot

class TestStudentCRUD:
    """
    Pruebas para HU-002, HU-003, HU-004, HU-005: Operaciones CRUD de Estudiantes
    """
    
    def test_create_student_success(self, logged_in_driver, wait):
        """
        HU-002 Camino feliz: Crear estudiante con datos válidos
        """
        try:
            # Ir a la página de crear estudiante
            logged_in_driver.get(f"{TestConfig.BASE_URL}/students/new")
            
            # Llenar formulario con datos válidos
            student_id = f"EST{int(time.time())}"  # ID único basado en timestamp
            
            # Campos requeridos
            logged_in_driver.find_element(By.NAME, "student_id").send_keys(student_id)
            logged_in_driver.find_element(By.NAME, "first_name").send_keys("Juan")
            logged_in_driver.find_element(By.NAME, "last_name").send_keys("Pérez")
            logged_in_driver.find_element(By.NAME, "email").send_keys("juan.perez@test.com")
            
            # Campos opcionales
            logged_in_driver.find_element(By.NAME, "phone").send_keys("809-123-4567")
            logged_in_driver.find_element(By.NAME, "date_of_birth").send_keys("1995-05-15")
            
            # Seleccionar carrera
            major_select = Select(logged_in_driver.find_element(By.NAME, "major"))
            major_select.select_by_visible_text("Ingeniería en Sistemas")
            
            logged_in_driver.find_element(By.NAME, "address").send_keys("Calle Principal #123, Santo Domingo")
            
            # Enviar formulario
            submit_button = logged_in_driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            submit_button.click()
            
            # Verificar redirección a lista de estudiantes
            wait.until(EC.url_contains("/students"))
            assert "/students" in logged_in_driver.current_url
            
            # Verificar mensaje de éxito
            success_message = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "alert-success")))
            assert "Estudiante creado exitosamente" in success_message.text
            
            take_screenshot(logged_in_driver, "test_create_student_success")
            
        except Exception as e:
            take_screenshot(logged_in_driver, "test_create_student_success_error")
            raise e
    
    def test_create_student_duplicate_id(self, logged_in_driver, wait):
        """
        HU-002 Prueba negativa: Crear estudiante con ID duplicado
        """
        try:
            # Primero crear un estudiante
            logged_in_driver.get(f"{TestConfig.BASE_URL}/students/new")
            
            student_id = f"EST{int(time.time())}"
            
            logged_in_driver.find_element(By.NAME, "student_id").send_keys(student_id)
            logged_in_driver.find_element(By.NAME, "first_name").send_keys("María")
            logged_in_driver.find_element(By.NAME, "last_name").send_keys("García")
            logged_in_driver.find_element(By.NAME, "email").send_keys("maria.garcia@test.com")
            
            submit_button = logged_in_driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            submit_button.click()
            
            # Esperar a que se cree el primer estudiante
            wait.until(EC.url_contains("/students"))
            
            # Ahora intentar crear otro con el mismo ID
            logged_in_driver.get(f"{TestConfig.BASE_URL}/students/new")
            
            logged_in_driver.find_element(By.NAME, "student_id").send_keys(student_id)  # Mismo ID
            logged_in_driver.find_element(By.NAME, "first_name").send_keys("Carlos")
            logged_in_driver.find_element(By.NAME, "last_name").send_keys("López")
            logged_in_driver.find_element(By.NAME, "email").send_keys("carlos.lopez@test.com")
            
            submit_button = logged_in_driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            submit_button.click()
            
            # Verificar mensaje de error
            error_message = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "alert-error")))
            assert "Error al crear estudiante" in error_message.text
            
            take_screenshot(logged_in_driver, "test_create_student_duplicate_id")
            
        except Exception as e:
            take_screenshot(logged_in_driver, "test_create_student_duplicate_id_error")
            raise e
    
    def test_create_student_invalid_email(self, logged_in_driver, wait):
        """
        HU-002 Prueba negativa: Crear estudiante con email inválido
        """
        try:
            logged_in_driver.get(f"{TestConfig.BASE_URL}/students/new")
            
            student_id = f"EST{int(time.time())}"
            
            logged_in_driver.find_element(By.NAME, "student_id").send_keys(student_id)
            logged_in_driver.find_element(By.NAME, "first_name").send_keys("Ana")
            logged_in_driver.find_element(By.NAME, "last_name").send_keys("Rodríguez")
            logged_in_driver.find_element(By.NAME, "email").send_keys("email_invalido")  # Email inválido
            
            submit_button = logged_in_driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            submit_button.click()
            
            # Verificar mensaje de error
            error_message = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "alert-error")))
            assert "Error al crear estudiante" in error_message.text
            
            take_screenshot(logged_in_driver, "test_create_student_invalid_email")
            
        except Exception as e:
            take_screenshot(logged_in_driver, "test_create_student_invalid_email_error")
            raise e
    
    def test_view_students_list(self, logged_in_driver, wait):
        """
        HU-003 Camino feliz: Ver lista de estudiantes
        """
        try:
            # Ir a la lista de estudiantes
            logged_in_driver.get(f"{TestConfig.BASE_URL}/students")
            
            # Verificar que estamos en la página correcta
            assert "/students" in logged_in_driver.current_url
            
            # Verificar que existe la tabla de estudiantes
            table = wait.until(EC.presence_of_element_located((By.TAG_NAME, "table")))
            assert table.is_displayed()
            
            # Verificar que hay enlaces de acción
            action_links = logged_in_driver.find_elements(By.CSS_SELECTOR, "a[href*='/students/']")
            assert len(action_links) > 0
            
            # Verificar paginación si hay muchos estudiantes
            pagination = logged_in_driver.find_elements(By.CSS_SELECTOR, ".pagination")
            if pagination:
                assert pagination[0].is_displayed()
            
            take_screenshot(logged_in_driver, "test_view_students_list")
            
        except Exception as e:
            take_screenshot(logged_in_driver, "test_view_students_list_error")
            raise e
    
    def test_edit_student_success(self, logged_in_driver, wait):
        """
        HU-004 Camino feliz: Editar estudiante con datos válidos
        """
        try:
            # Primero crear un estudiante para editar
            logged_in_driver.get(f"{TestConfig.BASE_URL}/students/new")
            
            student_id = f"EST{int(time.time())}"
            
            logged_in_driver.find_element(By.NAME, "student_id").send_keys(student_id)
            logged_in_driver.find_element(By.NAME, "first_name").send_keys("Pedro")
            logged_in_driver.find_element(By.NAME, "last_name").send_keys("Martínez")
            logged_in_driver.find_element(By.NAME, "email").send_keys("pedro.martinez@test.com")
            
            submit_button = logged_in_driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            submit_button.click()
            
            # Esperar a que se cree y redirija
            wait.until(EC.url_contains("/students"))
            
            # Ir a la lista y hacer click en editar
            logged_in_driver.get(f"{TestConfig.BASE_URL}/students")
            
            # Buscar el enlace de editar para el estudiante creado
            edit_links = logged_in_driver.find_elements(By.CSS_SELECTOR, "a[href*='/edit']")
            if edit_links:
                edit_links[0].click()
                
                # Verificar que estamos en el formulario de edición
                wait.until(EC.url_contains("/edit"))
                
                # Modificar algunos campos
                first_name_field = logged_in_driver.find_element(By.NAME, "first_name")
                first_name_field.clear()
                first_name_field.send_keys("Pedro Actualizado")
                
                # Enviar formulario
                submit_button = logged_in_driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
                submit_button.click()
                
                # Verificar mensaje de éxito
                success_message = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "alert-success")))
                assert "Estudiante actualizado exitosamente" in success_message.text
                
                take_screenshot(logged_in_driver, "test_edit_student_success")
            
        except Exception as e:
            take_screenshot(logged_in_driver, "test_edit_student_success_error")
            raise e
    
    def test_delete_student_success(self, logged_in_driver, wait):
        """
        HU-005 Camino feliz: Eliminar estudiante con confirmación
        """
        try:
            # Primero crear un estudiante para eliminar
            logged_in_driver.get(f"{TestConfig.BASE_URL}/students/new")
            
            student_id = f"EST{int(time.time())}"
            
            logged_in_driver.find_element(By.NAME, "student_id").send_keys(student_id)
            logged_in_driver.find_element(By.NAME, "first_name").send_keys("Eliminar")
            logged_in_driver.find_element(By.NAME, "last_name").send_keys("Test")
            logged_in_driver.find_element(By.NAME, "email").send_keys("eliminar.test@test.com")
            
            submit_button = logged_in_driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            submit_button.click()
            
            # Esperar a que se cree
            wait.until(EC.url_contains("/students"))
            
            # Ir a la lista y hacer click en eliminar
            logged_in_driver.get(f"{TestConfig.BASE_URL}/students")
            
            # Buscar el botón de eliminar
            delete_buttons = logged_in_driver.find_elements(By.CSS_SELECTOR, "button[data-bs-target*='deleteModal']")
            if delete_buttons:
                delete_buttons[0].click()
                
                # Esperar a que aparezca el modal de confirmación
                modal = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "modal")))
                assert modal.is_displayed()
                
                # Confirmar eliminación
                confirm_button = modal.find_element(By.CSS_SELECTOR, "button[type='submit']")
                confirm_button.click()
                
                # Verificar mensaje de éxito
                success_message = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "alert-success")))
                assert "Estudiante eliminado exitosamente" in success_message.text
                
                take_screenshot(logged_in_driver, "test_delete_student_success")
            
        except Exception as e:
            take_screenshot(logged_in_driver, "test_delete_student_success_error")
            raise e
    
    def test_create_student_empty_required_fields(self, logged_in_driver, wait):
        """
        HU-002 Prueba de límites: Crear estudiante con campos requeridos vacíos
        """
        try:
            logged_in_driver.get(f"{TestConfig.BASE_URL}/students/new")
            
            # Dejar campos requeridos vacíos
            logged_in_driver.find_element(By.NAME, "student_id").send_keys("")  # Vacío
            logged_in_driver.find_element(By.NAME, "first_name").send_keys("")  # Vacío
            logged_in_driver.find_element(By.NAME, "last_name").send_keys("")   # Vacío
            logged_in_driver.find_element(By.NAME, "email").send_keys("")       # Vacío
            
            submit_button = logged_in_driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            submit_button.click()
            
            # Verificar que permanecemos en el formulario
            assert "/students/new" in logged_in_driver.current_url
            
            # Verificar mensaje de error
            error_message = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "alert-error")))
            assert "Error al crear estudiante" in error_message.text
            
            take_screenshot(logged_in_driver, "test_create_student_empty_required_fields")
            
        except Exception as e:
            take_screenshot(logged_in_driver, "test_create_student_empty_required_fields_error")
            raise e 