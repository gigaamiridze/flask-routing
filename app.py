from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/register')
def register():
    return "This is register page" # TODO Generalize

@app.route('/login')
def login():
    return "This is login page" # TODO Generalize

@app.route('/forgotten_password')
def forgotten_password():
    return "This is forgotten password functionality" # TODO Generalize

if __name__ == '__main__':
    app.run(debug=True, port=7777)
