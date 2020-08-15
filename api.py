from flask import Flask,jsonify,request

app = Flask(__name__)

user_sign_in_details=[
{
	'email':'abc@gmail.com',
	'password':'1234'
}

]

user_sign_up_details=[
{
	'firstname':'abc',
	'lastname':'def',
	'email':'abc@gmail.com',
	'password':'1234',
}

]


@app.route('/',methods ={'POST'})
def home():
	request_data =request.get_json()
	sign_in_details={
	'email':request_data['email'],
	'password':request_data['password']

	}

	user_sign_in_details.append(sign_in_details)
	return jsonify(sign_in_details)

@app.route('/')
def get_sign_in_details_home():
    return jsonify({'user_sign_in_details': user_sign_in_details})	

@app.route('/sign-in',methods={'POST'})
def sign_in():
	request_data =request.get_json()
	sign_in_details={
	'email':request_data['email'],
	'password':request_data['password']

	}

	user_sign_in_details.append(sign_in_details)
	return jsonify(sign_in_details)

@app.route('/sign-in')
def get_sign_in_details():
    return jsonify({'user_sign_in_details': user_sign_in_details})	

@app.route('/sign-up',methods={'POST'})
def sign_up():
	request_data =request.get_json()
	sign_up_details={
	'firstname':request_data['firstname'],
	'lastname':request_data['lastname'],
	'email':request_data['email'],
	'password':request_data['password']

	}

	user_sign_up_details.append(sign_up_details)
	return jsonify(sign_up_details)


@app.route('/sign-up')
def get_sign_up_details():
    return jsonify({'user_sign_up_details': user_sign_up_details})	


app.run(port=5000)