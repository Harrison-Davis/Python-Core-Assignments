from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
from flask_app import DATABASE, bcrypt

import re
instructions_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

date_made_REGEX = re.compile(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$')

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.recipe_name = data['recipe_name']
        self.under_30 = data['under_30']
        self.instructions = data['instructions']
        self.description = data['description']
        self.date_made = data['date_made']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL(DATABASE).query_db(query)
        recipes = []
        for dict in results:
            recipes.append( cls(dict) )
        return recipes

    @classmethod
    def create(cls, data:dict):
        query = "INSERT INTO recipes (recipe_name, under_30, instructions, description, date_made, user_id) VALUES (%(recipe_name)s, %(under_30)s, %(instructions)s, %(description)s, %(date_made)s, %(user_id)s);"
        result = connectToMySQL(DATABASE).query_db(query,data)
        return result

    @classmethod
    def get_one(cls,data):
        query  = "SELECT * FROM recipes WHERE id = %(id)s";
        results = connectToMySQL(DATABASE).query_db(query,data)
        if results:
            return cls(results[0])
        return False

    @classmethod
    def get_one_by_instructions(cls,data:dict):
        query  = "SELECT * FROM recipes WHERE instructions = %(instructions)s";
        results = connectToMySQL(DATABASE).query_db(query,data)
        if results:
            return cls(results[0])
        return False


    @classmethod
    def update_one(cls,data):
        query = "UPDATE recipes SET recipe_name=%(recipe_name)s,under_30=%(under_30)s,instructions=%(instructions)s, date_made=%(date_made)s, updated_at=NOW() WHERE id=%(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)


    @classmethod
    def destroy(cls,data):
        query  = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)



    #Validate recipe-------

    @staticmethod
    def validate_recipe(data:dict) -> None:
        is_valid = True

        if len(data['recipe_name']) < 1:
            is_valid = False
            flash('Name is required')
        if len(data['description']) < 1:
            is_valid = False
            flash('Description is required')
        if len(data['instructions']) < 1:
            is_valid = False
            flash('Instructions are required')
        if len(data['date_made']) < 1:
            is_valid = False
            flash('Date Made is required')
        if len(data['under_30']) < 1:
            is_valid = False
            flash('Selection is required')
        return is_valid

