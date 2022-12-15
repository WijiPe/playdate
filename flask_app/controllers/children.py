from flask import render_template, redirect, request, session
from flask_app.models.users import User
from flask_app.models.children import Child
from flask_app import app
from flask_bcrypt import Bcrypt
# from flask import flash
bcrypt = Bcrypt(app)


@app.route("/to_add_child")
def to_add_child():
    if 'id' not in session:
        return {'status': 'fail', 'reason': 'invalid'},400
    return {'status': 'success'}

@app.post('/add_child')
def add_child():
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
        "user_id" : request.form['user_id'],
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "date_of_birth" : request.form['date_of_birth'],
        "picture_profile" : request.form['picture_profile'],
        "allergy" : request.form['allergy'],
        "medicine" : request.form['medicine'],
        "favourite_thing" : request.form['favourite_thing'],
        "additional_information" : request.form['additional_information'],
        }
    Child.add_child(data)
    return {'status': 'success'}

@app.route("/child/<int:child_id>")
def show_child(child_id):
    # if 'id' not in session:
    #     return {'status': 'success'}
    data = {
        "child_id":child_id,
        "id": session['id']
    }
    child = Child.get_child_by_user_and_childId(data)
    return {'status': 'success'}
