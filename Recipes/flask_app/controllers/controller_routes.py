from flask_app import app, bcrypt
from flask import render_template, request, redirect, session
from flask_app.models import model_user, model_recipe


#redirect to login page
@app.route('/')
def login():
    #stops logged in user from trying to login
    if 'uuid' in session:
        return redirect('/user/recipes')

    return render_template('login.html')



@app.route('/user/recipes')
def dashboard():
    #keeps logged out user from reaching this site
    if 'uuid' not in session:
        return redirect('/')

    context = {
        'user': model_user.User.get_one({'id':session['uuid']}),
        'all_recipes': model_recipe.Recipe.get_all()
    }
    return render_template('user_recipes.html', **context)


