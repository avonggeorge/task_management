"""
This file defines the routes to the sections of the application
"""
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from . import db
from .models import User, Todos
from datetime import datetime



routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    return render_template('home.html', user=current_user)



@routes.route('/form', methods=['POST', 'GET'])
@login_required
def form():
    # Code to handle form submission goes here
    if request.method == 'POST':
        # Retrieve data from the form
        item = request.form.get('item')
        description = request.form.get('description')
        location = request.form.get('location')
        date = request.form.get('date')
        status = request.form.get('status')
        notes = request.form.get('notes')

        new_task = Todos(
            item=item,
            status=status,
            notes=notes,
            description=description,
            location=location,
            date=datetime.strptime(date, '%Y-%m-%d'),
            user_id=current_user.id,
            )

        # Add the task to the database
        db.session.add(new_task)
        db.session.commit()

        print(status)

        flash('Task added successfully!', category='success')
        return redirect(url_for('routes.form'))

    user_task = Todos.query.filter_by(user_id=current_user.id).all()
    return render_template('form.html', tasks=user_task, user=current_user)


@routes.route('/delete/<int:task_id>', methods=['POST'])
@login_required
def delete(task_id):
    task = Todos.query.get_or_404(task_id)
    if task.user_id == current_user.id:
        db.session.delete(task)
        db.session.commit()
        flash('Task deleted successfully!', category='success')
    return redirect(url_for('routes.form'))

@routes.route('/update/<int:task_id>', methods=['POST'])
@login_required
def update(task_id):
    task = Todos.query.get_or_404(task_id)
    if task.user_id == current_user.id:
        # Get updated data from the request
        data = request.get_json()
        task.item = data.get('item', task.item)
        task.description = data.get('description', task.description)
        task.location = data.get('location', task.location)
        task.notes = data.get('notes', task.notes)
        task.status = data.get('status', task.status)
        task.date = datetime.strptime(data.get('date'), '%Y-%m-%d') if data.get('date') else task.date

        # Update the database
        db.session.commit()
        return {'message': 'Task updated successfully!'}, 200
    return {'message': 'Unauthorized'}, 403
