from flask.json import jsonify
from utils.JWTManager import JWTManager
from flask import Blueprint, request
from utils.ConfigReader import ConfigReader

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/auth', methods=['POST'])
def auth():
    data = request.json
    user = data['user']
    password = data['password']
    config = ConfigReader.create().get_dict_by_section('MASTER')
    
    if user == config['user'] and password == config['password']:
        user_data = {'role':'ADMIN', 'name': user}
        user_data['token'] = JWTManager().encode(user_data)
        return jsonify(user_data), 200
    
    raise 'Not implemented yet'