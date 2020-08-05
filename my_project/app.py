from flask import Flask,render_template,url_for
app = Flask(__name__)

reviews =[
{
	'title':'What is meaning ?',
	'name':'Pasindu',
	'comment':'Nothing right Now',
	'date_posted':'12th June 2020',
},
{
	'title':'What is meaning ?',
	'name':'John Smith',
	'comment':'Dont have any idea now',
	'date_posted':'25th June 2020',
},
]

@app.route('/')
def hello_world():
	return "<h1>Hello World</h1>"

@app.route('/home')
def home():
	return render_template('home.html',reviews=reviews)

@app.route('/about')
def about():
	return render_template('about.html')