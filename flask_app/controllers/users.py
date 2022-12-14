from flask import redirect, request, session
from flask_app.models.users import User
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.post('/register')
def register():
    if User.is_valid(request.form):
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        data = {
            "first_name" : request.form['first_name'],
            "last_name" : request.form['last_name'],
            "email_address" : request.form['email_address'],
            "location" : request.form['location'],
            "phone_number" : request.form['phone_number'],
            "password" : pw_hash
        }
        id = User.register(data)
        session['id'] = id
        return {'status': 'success'}
    return {'status': 'fail', 'reason': 'invalid'},400