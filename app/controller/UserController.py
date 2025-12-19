from app.model import User
from app import response, db
from flask import request

def index():
    try:
        users = User.query.all()
        data = transform(users)
        return response.ok(data, "")
    except Exception as e:
        print(e)
        return response.badRequest([], "An error occurred")

def store():
    try:
        name = request.json['name']
        email = request.json['email']
        password = request.json['password']

        user = User(name=name, email=email)
        user.set_password(password)
        
        db.session.add(user)
        db.session.commit()

        return response.ok(singleTransform(user), "User created successfully")
    except Exception as e:
        print(e)
        return response.badRequest([], "Failed to create user")

def show(id):
    try:
        user = User.query.filter_by(id=id).first()
        if not user:
            return response.badRequest([], 'User not found')
        
        data = singleTransform(user)
        return response.ok(data, "")
    except Exception as e:
        print(e)
        return response.badRequest([], "An error occurred")

def update(id):
    try:
        user = User.query.filter_by(id=id).first()
        if not user:
            return response.badRequest([], 'User not found')

        json_data = request.json
        if 'name' in json_data:
            user.name = json_data['name']
        if 'email' in json_data:
            user.email = json_data['email']
        if 'password' in json_data:
            user.set_password(json_data['password'])

        db.session.commit()
        return response.ok(singleTransform(user), "User updated successfully")
    except Exception as e:
        print(e)
        return response.badRequest([], "Failed to update user")

def delete(id):
    try:
        user = User.query.filter_by(id=id).first()
        if not user:
            return response.badRequest([], 'User not found')

        db.session.delete(user)
        db.session.commit()
        return response.ok([], "User deleted successfully")
    except Exception as e:
        print(e)
        return response.badRequest([], "Failed to delete user")

def transform(users):
    array = []
    for i in users:
        array.append(singleTransform(i))
    return array

def singleTransform(user):
    data = {
        'id': user.id,
        'name': user.name,
        'email': user.email
    }
    return data
