from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # enable CORS on all routes

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api/users')
def get_users():
    return {
        'users': [
            {
                'id': 1,
                'name': 'Alice'
            }, 
            {
                'id': 2,
                'name': 'Bob'
            }, 
            {
                'id': 3,
                'name': 'Juan'
            }
        ]
    }

@app.route('/api/fruits')
def get_fruits():
    return ['Apple', 'Banana', 'Cherry']

if __name__ == '__main__':
    app.run(debug=True) # by default, Flask runs on port 5000
