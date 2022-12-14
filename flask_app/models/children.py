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

    # @classmethod
    # def get_cars_show_owner(cls):
    #     query = "SELECT * FROM cars JOIN users ON users.id = cars.user_id;"
    #     results = connectToMySQL(DB).query_db(query)
    #     print(results)
    #     car = []
    #     for result in results:
    #         car.append(cls(result))
    #     return car