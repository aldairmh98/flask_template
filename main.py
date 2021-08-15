from flask import Flask
from users.controller.usersController import users_blueprint
app = Flask(__name__)

@app.route('/', methods=['GET'])
def welcome():
    return 'Hello world'

app.register_blueprint(users_blueprint)

if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')
