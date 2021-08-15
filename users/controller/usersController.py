from flask import Blueprint, request, jsonify

users_blueprint = Blueprint('users', __name__)

@users_blueprint.route('/users', methods=['GET'])
def get_users():
    return 'Getting users'

@users_blueprint.route('/users', methods=['POST'])
def create_user():
    data = request.json
    return jsonify(data), 200