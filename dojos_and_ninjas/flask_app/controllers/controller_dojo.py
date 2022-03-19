from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.model_dojo import Dojo
from flask_app.models.model_ninja import Ninja


#route to main dojo page
@app.route('/')
def get_all():
    return redirect('/dojos')

#display main dojo page
@app.route('/dojos')
def dojos():
    return render_template("dojo.html",dojos=Dojo.get_all())

#action - create new dojo and return results back to to dojo page
@app.route('/dojo/create',methods=['POST'])
def create_dojo():
    Dojo.create(request.form)
    return redirect('/dojos')

# display - render Dojos_ninjas page
@app.route('/dojos_ninjas/<int:id>')
def dojos_ninjas(id):
    data ={
        "id":id
    }
    return render_template('dojos_ninjas.html', dojo=Dojo.get_one(data), ninjas=Ninja.get_all_ninjas_by_dojo_id(data))





