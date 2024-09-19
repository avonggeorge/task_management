"""
This file handles user authentication, ie. signin|signup
"""

from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, logout_user, login_required, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    # Process login logic
    if request.method == 'POST':
        email  = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Loggin successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('routes.form'))
            else:
                flash('Incorrect password, pls try again', category='error')
        else:
            flash('User does not exist!', category='error')

    data = request.form
    print(data)
    return render_template('login.html', user=current_user)
@auth.route('/logout', methods=['GET', 'POST'])
def logout():
    # Code to handle logout functionality goes here
    logout_user()
    return redirect(url_for('auth.login'))
@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Validate form data here
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm = request.form.get('confirm-password')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists', category='error')
        # validate the form data
        elif len(name) < 3:
            flash('Name must be at least 3 characters', category="error")
        elif len(email) < 3:
            flash('Email must be at least 3 characters', category="error")
        elif password != confirm:
            flash('Passwords do not match', category="error")
        elif len(password) < 6:
            flash('Password must be at least 6 characters', category="error")
        else:
            # add user to database
            new_user = User(email=email, name=name, password=generate_password_hash(password, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created successfully', category="success")
            login_user(new_user, remember=True)
            return redirect(url_for('routes.form'))

    # Code to handle signup functionality goes here
    return render_template('signup.html', user=current_user)