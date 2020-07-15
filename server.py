from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/about.html')
def hello_world():
    return render_template('about.html')

hello_world()

@app.route('/blog')
def blog():
    return 'Hello,This is my blog :)'

@app.route('/blog/2020/dog')
def blog():
    return 'Hello,This is my dog ,"sheery" :)'

hello_world()


#py -m venv env
#env/Scripts/activate
#pip install flask
#set Flask_app={server.py}this is the python file name
#flask run
#set FLASK_ENV=development
#flask run