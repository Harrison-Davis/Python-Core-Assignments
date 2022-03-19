from flask_app.config.mysqlconnection import connectToMySQL

DATABASE = 'dojos_and_ninjas_db'

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(DATABASE).query_db(query)
        dojos = []
        for d in results:
            dojos.append( cls(d) )
        return dojos

    @classmethod
    def create(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        result = connectToMySQL(DATABASE).query_db(query,data)
        return result

    @classmethod
    def get_one(cls,data):
        query  = "SELECT * FROM dojos WHERE id = %(id)s";
        result = connectToMySQL(DATABASE).query_db(query,data)
        return cls(result[0])




