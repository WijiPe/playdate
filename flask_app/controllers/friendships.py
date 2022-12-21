from flask import render_template, redirect, request, session
from flask_app.models.users import User
from flask_app.models.children import Child
from flask_app.models.friendships import Friend
from flask_app import app
from flask_bcrypt import Bcrypt
# from flask import flash
bcrypt = Bcrypt(app)

@app.post('/add_friend/<int:id>')
def add_friend(id):
    # if 'id' not in session:
    #     return {'status': 'fail', 'reason': 'invalid'},400
    # if Child.is_valid(request.form):
    #     data = {
    #         'user_id': session['id'],
    #         **request.form
    #     }
    #     Child.add_child(data)
        # return {'status': 'success'}
    data = {
        # 'user_id': session['id'],
        "friend1_id" : id,
        "friend2_id1" : request.form['friend2_id1'],
        }
    Friend.add_friend(data)
    return {'status': 'success'}


@app.route("/get_child_friends/<int:child_id>")
def show_child_friends(child_id):
    # if 'id' not in session:
    #     return {'status': 'success'}
    data = {
        "id":child_id,
        # "id": session['id']
    }
    friendship = Friend.get_child_friends_by_childId(data)
    return {'status': 'success'}
