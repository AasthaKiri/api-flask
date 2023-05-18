# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'  

# @app.route('/contact')
# def contact():
#     return 'Contact us'  

# if __name__ == "__main__":
#     app.run(debug=True , port=8000)



# from flask import Flask, jsonify, request

# app = Flask(__name__)

# # Define a simple API route
# @app.route('/hello', methods=['GET'])
# def hello():
#     return jsonify({'message': 'Hello World!'})

# # Define a route that accepts parameters
# @app.route('/greet/<name>', methods=['GET'])
# def greet(name):
#     return jsonify({'message': 'Hello {}'.format(name)})

# # Define a route that accepts POST requests
# @app.route('/add', methods=['POST'])
# def add():
#     data = request.json
#     num1 = data['num1']
#     num2 = data['num2']
#     result = num1 + num2
#     return jsonify({'result': result})

# if __name__ == '__main__':
#     app.run(debug=True)



from flask import Flask
from flask_apispec import FlaskApiSpec
from Controller.DemoController import api as demo_api
from Controller.AdminUserController import admin as admin_user

app = Flask(__name__)
app.register_blueprint(demo_api, name='demo_api', url_prefix='/api')
app.register_blueprint(admin_user, name='admin_user', url_prefix='/AdminUser')

if __name__ == '__main__':
    app.run(debug=True)


