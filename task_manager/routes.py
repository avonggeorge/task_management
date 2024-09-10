"""
This file defines the routes to the sections of the application
"""
from flask import Blueprint, render_template

routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    return render_template('home.html')



@routes.route('/form')
def form():
    return render_template('form.html')


