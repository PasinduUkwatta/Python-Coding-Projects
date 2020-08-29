from flask import Flask, request, jsonify,flash
import mysql.connector
from flask_cors import CORS,cross_origin
from mysql.connector import Error
import bcrypt

app = Flask(__name__)
CORS(app)
app.config['JSON_ADD_STATUS'] = True


@app.route('/sign-in', methods=['POST'])
def sign_in():
    result = [{'msg': 'success'}, {'stat': '200 ok'}]
    if request.method == 'POST':
        sign_in_details= request.get_json()
        email = sign_in_details['email']
        password = sign_in_details['password']
     
        connection = mysql.connector.connect(host="localhost", user="root", password="1234", database="mydb")
        mycursor = connection.cursor()
        query = "INSERT INTO  sign_in(email, password) VALUES (%s,%s)"
        val = (email, password)
        mycursor.execute(query, val)
        connection.commit()
        return jsonify({'result': result})


@app.route('/sign-up', methods=['POST'])
def sign_up():
    result = [{'msg': 'success'}, {'stat': '200 ok'}]
    if request.method == 'POST':
        sign_up_details= request.get_json()
        firstname = sign_up_details['firstname']
        lastname = sign_up_details['lastname']
        email = sign_up_details['email']
        password = sign_up_details['password']
     
        connection = mysql.connector.connect(host="localhost", user="root", password="1234", database="mydb")
        mycursor = connection.cursor()
        query = "INSERT INTO  users(first_name,last_name,email, password) VALUES (%s,%s,%s,%s)"
        val = (firstname, lastname,email, password)
        mycursor.execute(query, val)
        connection.commit()
        return jsonify({'result': result})

@app.route("/sign-in-get",methods=['GET'])
def sign_in_get():
    sign_in_get_details= request.get_json()
    email = sign_in_get_details['email']
    password = sign_in_get_details['password']
  
    connection = mysql.connector.connect(host="localhost", user="root", password="1234", database="sample_project_db")
    mycursor = connection.cursor()
    sql="SELECT * FROM users WHERE email ='pasindu.17@itfac.mrt.ac.lk'"

    mycursor.execute(sql)
    results= mycursor.fetchall()
    return jsonify(results)
