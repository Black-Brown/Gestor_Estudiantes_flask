from flask import Blueprint, render_template
from flask_login import login_required
from models.student import Student

dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/')
@dashboard.route('/dashboard')
@login_required
def index():
    # Obtener estadísticas básicas
    total_students = Student.query.count()
    active_students = Student.query.filter_by(is_active=True).count()
    recent_students = Student.query.order_by(Student.enrollment_date.desc()).limit(5).all()

    return render_template('dashboard/index.html',
                           total_students=total_students,
                           active_students=active_students,
                           recent_students=recent_students) 