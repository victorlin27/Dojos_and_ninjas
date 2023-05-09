from flask_app.config.mysqlconnection import connectToMySQL
import pprint
from flask_app.models.ninja_model import Ninja

db = 'dojos_ninjas'

class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
    
    @classmethod
    def save(cls,data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s)"
        return connectToMySQL(db).query_db(query,data)

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM  dojos'
        results = connectToMySQL(db).query_db(query)
        all_dojos =[]
        pprint.pprint(results)
        for dojo in results:
            all_dojos.append(cls(dojo))
        return all_dojos

    @classmethod
    def get_one_dojo(cls,data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id where dojos.id = %(id)s"
        results = connectToMySQL(db).query_db(query,data)
        pprint.pprint(results, sort_dicts=False)
        dojos = cls(results[0])
        for ninja in results:
            ninja_dictionary = {
                'id' : ninja['ninjas.id'],
                'first_name' :ninja['first_name'],
                'last_name' :ninja['last_name'],
                'age' : ninja['age'],
                'created_at' :ninja['ninjas.created_at'],
                'updated_at' : ninja['ninjas.updated_at'],
            }
            dojos.ninjas.append(Ninja(ninja_dictionary))
        return dojos
