from flask_app import app, bcrypt
from flask import render_template, request, redirect, session
from flask_app.models.model_user import User



#action - create new user and return results back to to user page
@app.route('/user/create',methods=['POST'])
def create_user():
    #validate user
    is_valid = User.validate_registration(request.form)

    if not is_valid:
        return redirect('/')
    #if is valid - move on to hash password
    hash_pw = bcrypt.generate_password_hash(request.form['pw'])
    data = {
        **request.form,
        'pw': hash_pw
    }
    #create user
    id = User.create(data)
    session['uuid'] = id
    return redirect('/')


@app.route('/user/login', methods=["POST"])
def user_login():
    #validate
    is_valid = User.validate_login(request.form)

    if not is_valid:
        return redirect('/')
    return redirect('/')


@app.route('/logout')
def user_logout():
    del session['uuid']
    return redirect('/')




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
