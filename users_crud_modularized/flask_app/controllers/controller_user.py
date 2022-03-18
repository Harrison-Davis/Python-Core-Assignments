from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.model_user import User

@app.route('/')
def index():
    return redirect('/users')


@app.route('/users')
def users():
    return render_template("users.html",users=User.get_all())


@app.route('/user/add')
def new():
    return render_template("add_user.html")

@app.route('/user/create',methods=['POST'])
def create_user ():
    User.create(request.form)
    return redirect('/users')


@app.route('/user/edit/<int:id>')
def edit(id):
    data ={ 
        "id":id
    }
    return render_template("edit_user.html",user=User.get_one(data))

@app.route('/user/show/<int:id>')
def show(id):
    data ={ 
        "id":id
    }
    return render_template("show_user.html",user=User.get_one(data))


@app.route('/user/update',methods=['POST'])
def user_update():
    User.update_one(request.form)
    return redirect('/users')

@app.route('/user/destroy/<int:id>')
def destroy(id):
    data ={
        'id':id
    }
    User.destroy(data)
    return redirect('/users')

