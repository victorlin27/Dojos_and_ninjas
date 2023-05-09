from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.dojo_model import Dojo

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def home():
    dojos = Dojo.get_all()
    return render_template('home.html', all_dojos = dojos)

@app.route('/create_dojo', methods = ['post'])
def create_dojo():
    dojos = Dojo.save(request.form)
    return redirect('/dojos')

@app.route('/get_one_dojo/<int:id>')
def show_one_dojo(id):
    data = {
        'id': id
    }
    return render_template('show_dojo.html', one_dojo = Dojo.get_one_dojo(data) )
