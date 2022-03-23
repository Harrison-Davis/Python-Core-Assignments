from flask_app import app, bcrypt
from flask import render_template, request, redirect, session
from flask_app.models import model_recipe
from flask_app.models.model_recipe import Recipe
from flask_app.models.model_user import User



#action - create new recipe and return results back to to recipe page

#------display page------
@app.route('/recipes/addnewrecipe')
def add_new_recipe():           
    return render_template('add_new_recipe.html')


#----display page-----
@app.route('/recipe/edit/<int:id>')
def edit_recipe(id):
    data={
        'id':id
    }
    return render_template('edit_recipe.html',recipe=Recipe.get_one(data))

#----display page view instructions-----
@app.route('/recipes/view_instructions/<int:id>')
def view_instructions(id):
    data={
        "id":id
    }
    return render_template('view_instructions.html', recipe=Recipe.get_one(data))


#-----action:update recipe-------
@app.route('/recipe/update/<int:id>', methods=['POST'])
def recipe_update(id):
    data ={ **request.form,
        "id":id
    }
    Recipe.update_one(data)
    return redirect('/user/recipes')




#-----action create recipe-------
@app.route('/recipes/create', methods=['POST'])
def create_recipe():
    #validations
    is_valid = model_recipe.Recipe.validate_recipe(request.form)
    if not is_valid:
        return redirect('/recipes/addnewrecipe')
    data = {**request.form,
        'user_id': session['uuid']
    }
    model_recipe.Recipe.create(data)
    return redirect('/')


#-----action delete recipe-------
@app.route('/recipe/destroy/<int:id>')
def destroy_recipe(id):
    data ={
        'id':id
    }
    Recipe.destroy(data)
    return redirect('/user/recipes')
