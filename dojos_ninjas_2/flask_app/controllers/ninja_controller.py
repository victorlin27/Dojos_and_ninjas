from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.dojo_model import Dojo
from flask_app.models.ninja_model import Ninja

@app.route('/create_ninja')
def show_create_ninja_page():
    dojos = Dojo.get_all()
    return render_template('create_ninja.html',dojos = dojos)

@app.route('/create_ninja', methods = ['post'])
def create_ninja():
    Ninja.save(request.form)
    dojo_id = request.form['dojo_id']
    return redirect(f'/get_one_dojo/{dojo_id}')

@app.route('/home')
def go_home():
    return redirect('/dojos')

