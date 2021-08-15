from re import S
from utils.ConfigReader import ConfigReader
from users.repository.usersRepository import UserRepository
from flask import Blueprint, request, jsonify

users_blueprint = Blueprint('users', __name__)

@users_blueprint.route('/users', methods=['GET'])
def get_users():
    user_repository = UserRepository(ConfigReader.create())
    result = user_repository.find_all()
    return jsonify([{'id':str(r.get('_id')),'name': r.get('name')} for r in result]), 200 

@users_blueprint.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user_repository = UserRepository(ConfigReader.create())
    user_repository.create(data.get('name'))
    result = user_repository.find_all()
    return jsonify([{'id':str(r.get('_id')),'name': r.get('name')} for r in result]), 200 


@users_blueprint.route('/users/<id>', methods=['DELETE'])
def delete(id: str):
    user_repository = UserRepository(ConfigReader.create())
    user_repository.remove(id)
    return jsonify({}), 200
