from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required
from models.student import Student
from models.database import db
from datetime import datetime

students = Blueprint('students', __name__)

@students.route('/')
@login_required
def index():
    page = request.args.get('page', 1, type=int)
    per_page = 10
    
    students_list = Student.query.paginate(
        page=page, per_page=per_page, error_out=False
    )
    
    return render_template('students/index.html', students=students_list)

@students.route('/new', methods=['GET', 'POST'])
@login_required
def new():
    if request.method == 'POST':
        try:
            student = Student(
                student_id=request.form['student_id'],
                first_name=request.form['first_name'],
                last_name=request.form['last_name'],
                email=request.form['email'],
                phone=request.form.get('phone'),
                date_of_birth=datetime.strptime(request.form['date_of_birth'], '%Y-%m-%d').date() if request.form.get('date_of_birth') else None,
                major=request.form.get('major'),
                address=request.form.get('address')
            )
            
            db.session.add(student)
            db.session.commit()
            
            flash('Estudiante creado exitosamente', 'success')
            return redirect(url_for('students.index'))
            
        except Exception as e:
            db.session.rollback()
            flash(f'Error al crear estudiante: {str(e)}', 'error')
    
    return render_template('students/new.html')

@students.route('/<int:id>')
@login_required
def show(id):
    student = Student.query.get_or_404(id)
    return render_template('students/show.html', student=student)

@students.route('/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit(id):
    student = Student.query.get_or_404(id)
    
    if request.method == 'POST':
        try:
            student.student_id = request.form['student_id']
            student.first_name = request.form['first_name']
            student.last_name = request.form['last_name']
            student.email = request.form['email']
            student.phone = request.form.get('phone')
            student.date_of_birth = datetime.strptime(request.form['date_of_birth'], '%Y-%m-%d').date() if request.form.get('date_of_birth') else None
            student.major = request.form.get('major')
            student.address = request.form.get('address')
            
            db.session.commit()
            
            flash('Estudiante actualizado exitosamente', 'success')
            return redirect(url_for('students.show', id=student.id))
            
        except Exception as e:
            db.session.rollback()
            flash(f'Error al actualizar estudiante: {str(e)}', 'error')
    
    return render_template('students/edit.html', student=student)

@students.route('/<int:id>/delete', methods=['POST'])
@login_required
def delete(id):
    student = Student.query.get_or_404(id)
    
    try:
        db.session.delete(student)
        db.session.commit()
        flash('Estudiante eliminado exitosamente', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error al eliminar estudiante: {str(e)}', 'error')
    
    return redirect(url_for('students.index'))

@students.route('/<int:id>/toggle_status', methods=['POST'])
@login_required
def toggle_status(id):
    student = Student.query.get_or_404(id)
    
    try:
        student.is_active = not student.is_active
        db.session.commit()
        
        status = 'activado' if student.is_active else 'desactivado'
        flash(f'Estudiante {status} exitosamente', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error al cambiar estado: {str(e)}', 'error')
    
    return redirect(url_for('students.show', id=student.id))

@students.route('/api/students')
@login_required
def api_students():
    students_list = Student.query.all()
    return jsonify([student.to_dict() for student in students_list]) 