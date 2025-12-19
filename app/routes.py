from flask import Blueprint, request
from app.controller import UserController

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return "Hello from Flask!"

@bp.route('/users', methods=['POST', 'GET'])
def users():
    if request.method == 'GET':
        return UserController.index()
    else:
        return UserController.store()

@bp.route('/users/<id>', methods=['PUT', 'GET', 'DELETE'])
def usersDetail(id):
    if request.method == 'GET':
        return UserController.show(id)
    elif request.method == 'PUT':
        return UserController.update(id)
    elif request.method == 'DELETE':
        return UserController.delete(id)

@bp.route('/login', methods=['POST'])
def login():
    return UserController.login()
