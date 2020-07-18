from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!, Pasindu Python Flask Programming'

hello_world()

#py -m venv env
#env/Scripts/activate
#pip install flask
#set Flask_app={server.py}this is the python file name
#flask run
#set FLASK_ENV=development
#flask run

