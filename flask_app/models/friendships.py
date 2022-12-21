from flask_app.config.mysqlconnection import connectToMySQL
# from flask import flash
from flask_app.models.users import User

DB = "playdate"

class Friend:
    def __init__( self , data ):
        self.id = data['id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.friend1_id = data['friend1_id']
        self.friend2_id1 = data['friend2_id1']

    @classmethod
    def add_friend(cls, data):
        query = "INSERT INTO friendships (friend1_id, friend2_id1, updated_at, created_at) VALUES (%(friend1_id)s, %(friend2_id1)s, NOW(), NOW());"
        results = connectToMySQL(DB).query_db(query, data)
        return results


    @classmethod
    def get_child_friends_by_childId(cls,data):
        query = "SELECT * FROM children JOIN friendships ON children.id = friendships.friend1_id WHERE friendships.friend2_id1 = %(id)s;"
        results = connectToMySQL(DB).query_db(query,data)
        if results:
            one_child = cls(results[0])
            print('dic',results[0])
            print('object',results[0])
            return one_child

