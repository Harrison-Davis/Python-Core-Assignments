from multiprocessing.spawn import import_main_path
from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.model_ninja import Ninja
from flask_app.models.model_dojo import Dojo

@app.route('/ninjas')
def get_all_ninjas():
    return render_template("ninja.html",ninjas=Ninja.get_all())


@app.route('/ninja/add')
def new():
    return render_template("new_ninja.html", dojos=Dojo.get_all())


@app.route('/ninja/create', methods=['POST'])
def create_ninja():
    Ninja.create(request.form)

    dojo_id = request.form['dojo']
    return redirect(f'/dojos_ninjas/{dojo_id}')

