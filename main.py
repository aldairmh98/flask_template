from flask.json import jsonify
from utils.JWTManager import JWTManager
from utils.ConfigReader import ConfigReader
from utils.PyMongoConnection import PyMongoConnection
from flask import Flask, request
from users.controller.usersController import users_blueprint
from auth.controller.authController import auth_blueprint
app = Flask(__name__)

EXCLUDED_TOKEN_PATHS = ['/auth']

@app.route('/', methods=['GET'])
def welcome():
    return 'Hello world'

app.register_blueprint(users_blueprint)
app.register_blueprint(auth_blueprint)

@app.before_request
def before_request():
    path = request.path
    
    if path in EXCLUDED_TOKEN_PATHS:
        return
    
    auth = request.headers.get('Authorization')

    if auth is None:
        return jsonify({}), 401
    try:
        token = auth.replace('Bearer ', '')
        JWTManager().decode(token)
    except:
        return jsonify({'msg':'Bad Token'}), 401

if __name__ == '__main__':
    config = ConfigReader.create()
    mongo_connection = PyMongoConnection.create(config)
    app.run(debug=True, port=8080, host='0.0.0.0')
