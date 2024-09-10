"""
This file handles user authentication, ie. signin|signup
"""

from flask import Blueprint, render_template, request, flash, redirect, url_for

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    # Process login logic
    # if request.method == 'POST':
    #     if email != request.form.get('email'):
    #         flash('Incorrect Email address', category='error')
    #     elif password != request.form.get('password'):
    #         flash('Incorrect Password', category='error')
    #     elif 

    #     pass
    data = request.form
    print(data)
    return render_template('login.html')
@auth.route('/logout', methods=['GET', 'POST'])
def logout():
    # Code to handle logout functionality goes here
    return "Log out"

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Validate form data here
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm = request.form.get('confirm-password')

        # validate the form data
        if len(name) < 3:
            flash('Name must be at least 3 characters', category="error")
        elif len(email) < 3:
            flash('Email must be at least 3 characters', category="error")
        elif password != confirm:
            flash('Passwords do not match', category="error")
        elif len(password) < 6:
            flash('Password must be at least 6 characters', category="error")
        else:
            # add user to database
            flash('Account created successfully', category="success")

    # Code to handle signup functionality goes here
    return render_template('signup.html')