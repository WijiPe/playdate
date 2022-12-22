from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.users import User

DB = "playdate"

class Child:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.date_of_birth = data['date_of_birth']
        self.picture_profile = data['picture_profile']
        self.allergy = data['allergy']
        self.medicine = data['medicine']
        self.favourite_thing = data['favourite_thing']
        self.additional_information = data['additional_information']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def add_child(cls,data):
        query = """
            INSERT INTO children (first_name, last_name, date_of_birth, picture_profile, allergy, medicine, favourite_thing, additional_information, created_at, updated_at, user_id) 
            VALUE (%(first_name)s,%(last_name)s, %(date_of_birth)s, %(picture_profile)s, %(allergy)s, %(medicine)s, %(favourite_thing)s, %(additional_information)s, NOW(), NOW(), %(user_id)s);
        """
        results = connectToMySQL(DB).query_db(query,data)
        return results
    
    @classmethod
    def get_child_by_user_and_childId(cls,data):
        query = "SELECT * FROM children WHERE user_id = %(id)s AND children.id = %(child_id)s;"
        results = connectToMySQL(DB).query_db(query,data)
        if results:
            one_child = cls(results[0])
            print('dic',results[0])
            print('object',results[0])
            return one_child

    @classmethod
    def get_children_by_userId(cls,data):
        query = "SELECT * FROM children WHERE user_id = %(id)s;"
        results = connectToMySQL(DB).query_db(query,data)
        if results:
            all_children = cls(results[0])
            print('dic',results[0])
            print('object',results[0])
            return all_children
        
        # children = cls(results[0])

        # for row_from_db in results:
        #     user_data = {
        #         "id" : row_from_db["users.id"],
        #         "first_name" : row_from_db["first_name"],
        #         "last_name" : row_from_db["last_name"],
        #         "email" : row_from_db["email"],
        #         "phone_number" :data['phone_number'],
        #         "location" :data['location'],
        #         "password" : row_from_db["password"],
        #         "created_at" : row_from_db["users.created_at"],
        #         "updated_at" : row_from_db["users.updated_at"]
        #     }
        #     children.users.append(User(user_data))
        # return children

    @classmethod
    def get_one_child_by_id(cls,data):
        query = "SELECT * FROM children WHERE id = %(id)s;"
        results = connectToMySQL(DB).query_db(query,data)
        if results:
            one_child = cls(results[0])
            print('dic',results[0])
            print('object',results[0])
            return one_child