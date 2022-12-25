from flask_app.config.mysqlconnection import connectToMySQL
# from flask import flash
from flask_app.models.users import User

DB = "playdate"

class Playdate:
    def __init__( self , data ):
        self.id = data['id']
        self.playdate_type = data['playdate_type']
        self.date = data['date']
        self.location = data['location']
        self.host = data['host']
        self.information = data['information']
        self.dress_code = data['dress_code']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def add_playdate(cls,data):
        query = """
            INSERT INTO playdate (date, location, host, created_at, updated_at) 
            VALUE (%(date)s, %(location)s, %(host)s, NOW(), NOW());
        """
        results = connectToMySQL(DB).query_db(query,data)
        return results