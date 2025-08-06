# Pruebas Automatizadas con Selenium

Este proyecto contiene las pruebas automatizadas para el Sistema de Administración de Estudiantes desarrollado con Flask.

## 📋 Historias de Usuario Cubiertas

### HU-001: Autenticación de Usuario
- ✅ Login exitoso con credenciales correctas
- ❌ Login fallido con credenciales incorrectas
- ❌ Login con campos vacíos
- ✅ Logout exitoso

### HU-002: Crear Nuevo Estudiante
- ✅ Crear estudiante con datos válidos
- ❌ Crear estudiante con ID duplicado
- ❌ Crear estudiante con email inválido
- ❌ Crear estudiante con campos requeridos vacíos

### HU-003: Ver Lista de Estudiantes
- ✅ Ver lista de estudiantes con tabla y paginación

### HU-004: Editar Información de Estudiante
- ✅ Editar estudiante con datos válidos

### HU-005: Eliminar Estudiante
- ✅ Eliminar estudiante con confirmación modal

## 🚀 Instalación y Configuración

### 1. Instalar dependencias
```bash
cd selenium_tests
pip install -r requirements.txt
```

### 2. Instalar Chrome WebDriver
El proyecto usa `webdriver-manager` que descarga automáticamente el driver de Chrome.

### 3. Asegurar que la aplicación Flask esté ejecutándose
```bash
cd ../src
python main.py
```

La aplicación debe estar disponible en: `http://localhost:5000`

## 🧪 Ejecutar Pruebas

### Ejecutar todas las pruebas
```bash
python run_tests.py
```

### Ejecutar pruebas específicas
```bash
python run_tests.py test_authentication.py
python run_tests.py test_student_crud.py
```

### Ejecutar con pytest directamente
```bash
pytest test_authentication.py -v
pytest test_student_crud.py -v
pytest --html=reports/report.html --self-contained-html
```

## 📊 Reportes y Screenshots

### Reportes HTML
Los reportes se generan automáticamente en la carpeta `reports/` con:
- Resultados detallados de cada prueba
- Tiempo de ejecución
- Capturas de pantalla automáticas
- Información de errores

### Screenshots
Las capturas de pantalla se guardan en `screenshots/` con:
- Screenshots de pruebas exitosas
- Screenshots de errores para debugging
- Timestamp en el nombre del archivo

## 📁 Estructura del Proyecto

```
selenium_tests/
├── conftest.py              # Configuración de pytest y fixtures
├── test_authentication.py   # Pruebas de autenticación (HU-001)
├── test_student_crud.py     # Pruebas CRUD de estudiantes (HU-002-005)
├── run_tests.py             # Script para ejecutar pruebas
├── requirements.txt         # Dependencias de Python
├── README.md               # Esta documentación
├── reports/                # Reportes HTML generados
└── screenshots/            # Capturas de pantalla automáticas
```

## ⚙️ Configuración

### Credenciales por Defecto
- **Usuario:** `admin`
- **Contraseña:** `admin123`
- **URL Base:** `http://localhost:5000`

### Configuración de WebDriver
- **Navegador:** Chrome
- **Tiempo de espera implícito:** 10 segundos
- **Tiempo de espera explícito:** 10 segundos
- **Ventana:** Maximizada (1920x1080)

## 🔧 Personalización

### Cambiar URL de la aplicación
Editar `conftest.py`:
```python
class TestConfig:
    BASE_URL = "http://tu-servidor:puerto"
```

### Cambiar credenciales
Editar `conftest.py`:
```python
class TestConfig:
    ADMIN_USERNAME = "tu_usuario"
    ADMIN_PASSWORD = "tu_password"
```

### Agregar nuevas pruebas
1. Crear nuevo archivo `test_nuevo_modulo.py`
2. Importar fixtures necesarios de `conftest.py`
3. Usar la función `take_screenshot()` para capturas automáticas

## 📈 Tipos de Pruebas Implementadas

### Camino Feliz (Happy Path)
- Login exitoso
- Crear estudiante válido
- Ver lista de estudiantes
- Editar estudiante
- Eliminar estudiante

### Pruebas Negativas (Negative Testing)
- Login con credenciales incorrectas
- Crear estudiante con ID duplicado
- Crear estudiante con email inválido
- Login con campos vacíos

### Pruebas de Límites (Boundary Testing)
- Crear estudiante con campos requeridos vacíos
- Validación de formatos de datos

## 🐛 Solución de Problemas

### Error: ChromeDriver no encontrado
```bash
pip install webdriver-manager --upgrade
```

### Error: Elemento no encontrado
- Verificar que la aplicación Flask esté ejecutándose
- Revisar selectores CSS/XPath en las pruebas
- Aumentar tiempos de espera si es necesario

### Error: Puerto ocupado
Cambiar puerto en `src/main.py`:
```python
app.run(debug=True, port=5001)
```
Y actualizar `BASE_URL` en `conftest.py`

### Error: Dependencias faltantes
```bash
pip install -r requirements.txt --upgrade
```

## 📝 Notas Importantes

1. **Aplicación Flask debe estar ejecutándose** antes de ejecutar las pruebas
2. **Chrome debe estar instalado** en el sistema
3. **Conexión a internet** requerida para descargar ChromeDriver
4. **Permisos de escritura** necesarios para crear reportes y screenshots

## 🎯 Criterios de Evaluación Cumplidos

- ✅ **5 Historias de Usuario** con criterios de aceptación y rechazo
- ✅ **Pruebas automatizadas** con Selenium en Python
- ✅ **Camino feliz, negativas y límites** para cada flujo
- ✅ **Reporte HTML** con resultados detallados
- ✅ **Capturas de pantalla automáticas** de cada escenario
- ✅ **Documentación clara** y organizada
- ✅ **Código reutilizable** con fixtures y funciones auxiliares

## 📞 Soporte

Para problemas técnicos o dudas sobre las pruebas, revisar:
1. Logs de la aplicación Flask
2. Reportes HTML generados
3. Screenshots de errores
4. Documentación de Selenium y pytest 