from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


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