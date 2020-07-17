from flask import Flask,render_template,Response
app = Flask(__name__,template_folder = 'templates')
print(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/blog')
def blog():
    return 'Hello, Welcome to My Blog'

@app.route('/blog/2020')
def blog2():
    return 'Hello, My Dog is Sheery'


hello_world()


#py -m venv env
#env/Scripts/activate
#pip install flask
#set Flask_app={server.py}this is the python file name
#flask run
#set FLASK_ENV=development
#flask run