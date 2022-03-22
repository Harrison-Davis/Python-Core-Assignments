from flask_app import app, bcrypt
from flask import render_template, request, redirect, session
from flask_app.models import model_user


#redirect to login page
@app.route('/')
def login():
    if 'uuid' in session:
        return redirect('/dashboard')

    return render_template('login.html')



@app.route('/dashboard')
def dashboard():
    if 'uuid' not in session:
        return redirect('/')

    context = {
        'user': model_user.User.get_one({'id':session['uuid']})
    }
    return render_template('dashboard.html', **context)