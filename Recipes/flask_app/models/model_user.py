from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
from flask_app import DATABASE, bcrypt
from flask_app.models import model_recipe

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

PW_REGEX = re.compile(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$')

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.pw = data['pw']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(DATABASE).query_db(query)
        users = []
        for dict in results:
            users.append( cls(dict) )
        return users

    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, pw) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(pw)s);"
        result = connectToMySQL(DATABASE).query_db(query,data)
        return result

    @classmethod
    def get_one(cls,data:dict):
        query  = "SELECT * FROM users WHERE id = %(id)s";
        results = connectToMySQL(DATABASE).query_db(query,data)
        if results:
            return cls(results[0])
        return False

    @classmethod
    def get_one_by_email(cls,data:dict):
        query  = "SELECT * FROM users WHERE email = %(email)s";
        results = connectToMySQL(DATABASE).query_db(query,data)
        if results:
            return cls(results[0])
        return False


    @classmethod
    def update_one(cls,data):
        query = "UPDATE users SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s,updated_at=NOW() WHERE id=%(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)


    @classmethod
    def destroy(cls,data):
        query  = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)



    @classmethod
    def get_user_with_recipes(cls,data:dict):
        query = "SELECT * FROM users LEFT JOIN recipes ON user_id = recipes.user_id WHERE user_id=%(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if not results:
            return[]
        
        
        user = cls(results[0])
        user.recipe= []
        for dict in results:
            data ={
                'id': dict['recipes.id'],
                'recipe_name' : dict['recipe_name'],
                'under_30': dict['under_30'],
                'instructions': dict['instructions'],
                'description': dict['description'],
                'date_made': dict['date_made'],
                'created_at': dict['created_at'],
                'updated_at': dict['updated_at'],
                'user_id': dict['user_id']
            }
            recipe = model_recipe.Recipe(data)
            user.recipes.append(recipe)
        return user




#---------Validations--------
    @staticmethod
    def validate_registration(data:dict):
        is_valid = True
        if len(data['first_name']) < 2:
            is_valid = False
            flash("You must input a first name")
        if len(data['last_name']) < 2:
            is_valid = False
            flash("You must input a last name")
        if len(data['email']) < 2:
            is_valid = False
            flash("You must input an email")
        if not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email address!")
            is_valid = False
        else:
            potential_user = User.get_one_by_email({'email':data['email']})
            if potential_user:
                flash("There is already an account associated with this email.")
        if len(data['pw']) < 8:
            is_valid = False
            flash("You must input a password name")
        elif not PW_REGEX.match(data['pw']):
            is_valid = False
            flash('Min. 8 characters, 1 upper, 1 lower, 1 number, 1 special')
        if len(data['confirm_pw']) < 8:
            is_valid = False
            flash("You must input a confirm password")
        elif data['pw'] != data['confirm_pw']:
            is_valid = False
            flash('Passwords do not match')
        
        return is_valid


    @staticmethod
    def validate_login(data:dict):
        is_valid = True
        if len(data['email']) < 1:
            is_valid = False
            flash("Email is required")

        elif not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email address!")
            is_valid = False

        if len(data['pw']) < 1:
            is_valid = False
            flash("Password is required")

        else:
            potential_user = User.get_one_by_email({'email':data['email']})
            if not potential_user:
                flash("Invalid Credentials(email)")
            elif not bcrypt.check_password_hash(potential_user.pw, data['pw']):
                is_valid = False
                flash("Invalid Credentials(password)")
            else:
                session['uuid'] = potential_user.id
                
        return is_valid



