from flask_app.config.mysqlconnection import connectToMySQL
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.%]+@[a-zA-Z0-9.!&]+\.[a-zA-Z]+$')
PASSWORD_REGEX1 = re.compile (r'^.*[A-Z].*[0-9].*|.*[0-9].*[A-Z].*')

DB = "playdate"

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.lastname = data['lastname']
        self.email_address = data['email_address']
        self.phone_number = data['phone_number']
        self.location = data['location']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def register(cls, data):
        query = "INSERT INTO user (name, lastname, email_address, location, phone_number, password, updated_at, created_at) VALUES (%(name)s, %(lastname)s, %(email_address)s, %(location)s, %(phone_number)s,  %(password)s, NOW(), NOW());"
        results = connectToMySQL(DB).query_db(query, data)
        return results

    @staticmethod
    def is_valid(user):
        is_valid = True
        if len(user['name']) < 3:
            is_valid = False
        if len(user['lastname']) < 3:
            is_valid = False
        if not EMAIL_REGEX.match(user['email_address']):
            is_valid = False
        if len(user['password']) < 8:
            is_valid = False
        elif not PASSWORD_REGEX1.match(user['password']):
            is_valid = False
        return is_valid   