from flask import render_template, redirect, request, session
from flask_app.models.users import User
from flask_app.models.children import Child
from flask_app.models.friendships import Friend
from flask_app.models.playdates import Playdate
from flask_app import app
from flask_bcrypt import Bcrypt
# from flask import flash
bcrypt = Bcrypt(app)

@app.post('/add_playdate')
def add_playdate():
    # if 'id' not in session:
    #     return {'status': 'fail', 'reason': 'invalid'},400
    # if Child.is_valid(request.form):
    #     data = {
    #         'user_id': session['id'],
    #         **request.form
    #     }
    #     Child.add_child(data)
        # return {'status': 'success'}
    data1 ={
        "child_id": request.form['child_id'],
        "id": session['id']
    }
    if not Child.get_child_by_user_and_childId(data1):
        return {'status': 'fail', 'reason': 'invalid'},400
    data = {
        "date" : request.form['date'],
        "location" : request.form['location'],
        "information" : request.form['information'],
        "dress_code" : request.form['dress_code'],
        "playdate_type" : request.form['playdate_type'],
        "host" : session['child_id']
        }
    Playdate.add_playdate(data)
    return {'status': 'success'}