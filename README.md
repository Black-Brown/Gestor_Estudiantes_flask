# Sistema de Administración de Estudiantes

# by Jheinel Brown

Un sistema CRUD completo para la administración de estudiantes desarrollado con Flask, siguiendo el patrón MVC (Modelo-Vista-Controlador).

## Características

- ✅ **Autenticación de usuarios** con Flask-Login
- ✅ **CRUD completo** para estudiantes (Crear, Leer, Actualizar, Eliminar)
- ✅ **Base de datos SQLite** con SQLAlchemy
- ✅ **Interfaz moderna** con Bootstrap 5 y Font Awesome
- ✅ **Dashboard con estadísticas** en tiempo real
- ✅ **Paginación** en la lista de estudiantes
- ✅ **Validación de formularios** del lado servidor
- ✅ **Diseño responsive** para móviles y tablets
- ✅ **Mensajes flash** para feedback al usuario

## Estructura del Proyecto

```
first_flask/
├── src/
│   ├── controllers/          # Controladores (Lógica de negocio)
│   │   ├── auth.py          # Autenticación
│   │   ├── dashboard.py     # Dashboard principal
│   │   └── students.py      # CRUD de estudiantes
│   ├── models/              # Modelos de datos
│   │   ├── database.py      # Configuración de BD
│   │   ├── user.py          # Modelo de Usuario
│   │   └── student.py       # Modelo de Estudiante
│   ├── templates/           # Plantillas HTML
│   │   ├── base.html        # Layout principal
│   │   ├── auth/
│   │   │   └── login.html   # Página de login
│   │   ├── dashboard/
│   │   │   └── index.html   # Dashboard principal
│   │   └── students/
│   │       ├── index.html   # Lista de estudiantes
│   │       ├── new.html     # Crear estudiante
│   │       ├── show.html    # Ver estudiante
│   │       └── edit.html    # Editar estudiante
│   └── main.py              # Aplicación principal
├── requirements.txt          # Dependencias
└── README.md               # Este archivo
```

## Instalación

### 1. Clonar o descargar el proyecto

### 2. Crear un entorno virtual (recomendado)
```bash
python -m venv venv
```

### 3. Activar el entorno virtual
**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 4. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 5. Ejecutar la aplicación
```bash
cd src
python main.py
```

La aplicación estará disponible en: `http://localhost:5000`

## Credenciales por Defecto

Al ejecutar la aplicación por primera vez, se crea automáticamente un usuario administrador:

- **Usuario:** `admin`
- **Contraseña:** `admin123`

## Funcionalidades

### 🔐 Autenticación
- Login seguro con encriptación de contraseñas
- Protección de rutas con `@login_required`
- Logout automático

### 👥 Gestión de Estudiantes
- **Crear:** Formulario completo con validación
- **Listar:** Tabla con paginación y filtros
- **Ver:** Vista detallada de cada estudiante
- **Editar:** Formulario pre-llenado
- **Eliminar:** Con confirmación modal
- **Activar/Desactivar:** Cambiar estado del estudiante

### 📊 Dashboard
- Estadísticas en tiempo real
- Lista de estudiantes recientes
- Accesos rápidos a funciones principales

### 🎨 Interfaz de Usuario
- Diseño moderno con Bootstrap 5
- Iconos de Font Awesome
- Responsive design
- Mensajes de feedback
- Modales de confirmación

## Modelo de Datos

### Usuario (User)
- `id`: Identificador único
- `username`: Nombre de usuario
- `email`: Correo electrónico
- `password_hash`: Contraseña encriptada
- `is_admin`: Rol de administrador

### Estudiante (Student)
- `id`: Identificador único
- `student_id`: ID de estudiante (único)
- `first_name`: Nombre
- `last_name`: Apellido
- `email`: Correo electrónico
- `phone`: Teléfono
- `date_of_birth`: Fecha de nacimiento
- `address`: Dirección
- `major`: Carrera
- `enrollment_date`: Fecha de registro
- `is_active`: Estado activo/inactivo

## Rutas de la Aplicación

| Ruta | Método | Descripción |
|------|--------|-------------|
| `/` | GET | Dashboard principal |
| `/auth/login` | GET/POST | Página de login |
| `/auth/logout` | GET | Cerrar sesión |
| `/students` | GET | Lista de estudiantes |
| `/students/new` | GET/POST | Crear estudiante |
| `/students/<id>` | GET | Ver estudiante |
| `/students/<id>/edit` | GET/POST | Editar estudiante |
| `/students/<id>/delete` | POST | Eliminar estudiante |
| `/students/<id>/toggle_status` | POST | Cambiar estado |

## Tecnologías Utilizadas

- **Backend:** Flask 3.1.1
- **Base de Datos:** SQLAlchemy + SQLite
- **Autenticación:** Flask-Login
- **Frontend:** Bootstrap 5, Font Awesome
- **Encriptación:** Werkzeug

## Personalización

### Cambiar Base de Datos
En `src/main.py`, modifica la línea:
```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
```

### Agregar Nuevas Carreras
En las plantillas `new.html` y `edit.html`, agrega opciones al select de carreras.

### Modificar Estilo
Edita los estilos CSS en `src/templates/base.html`.

## Solución de Problemas

### Error de dependencias
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Error de base de datos
Elimina el archivo `students.db` y reinicia la aplicación para recrear las tablas.

### Error de puerto ocupado
Cambia el puerto en `src/main.py`:
```python
app.run(debug=True, port=5001)
```

## Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature
3. Commit tus cambios
4. Push a la rama
5. Abre un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles. 