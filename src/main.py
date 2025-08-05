from flask import Flask, redirect, url_for
from flask_login import login_required, current_user
import os

# Import models
from models.database import init_app, db
from models.user import User
# from models.student import Student

# Import controllers
from controllers.auth import auth
# from controllers.dashboard import dashboard
# from controllers.students import students

def create_app():
    app = Flask(__name__)
    
    # Configuración
    app.config['SECRET_KEY'] = 'tu-clave-secreta-aqui-cambiala-en-produccion'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Inicializar extensiones
    init_app(app)
    
    # Registrar blueprints
    app.register_blueprint(auth, url_prefix='/auth')
    # app.register_blueprint(dashboard, url_prefix='/dashboard')
    # app.register_blueprint(students, url_prefix='/students')
    
    # Ruta raíz
    @app.route('/')
    def index():
        if current_user.is_authenticated:
            return redirect(url_for('dashboard.index'))
        else:
            return redirect(url_for('auth.login'))
    
    # Crear tablas de base de datos
    with app.app_context():
        db.create_all()
        
        # Crear usuario administrador por defecto si no existe
        admin_user = User.query.filter_by(username='admin').first()
        if not admin_user:
            admin_user = User(
                username='admin',
                email='admin@example.com',
                is_admin=True
            )
            admin_user.set_password('admin123')
            db.session.add(admin_user)
            db.session.commit()
            print("Usuario administrador creado: admin / admin123")
    
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=5000)


