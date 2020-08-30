from flask import Flask, request, jsonify,flash
import mysql.connector
from flask_cors import CORS,cross_origin
from mysql.connector import Error
import bcrypt
from werkzeug.security import generate_password_hash,check_password_hash


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

        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        connection = mysql.connector.connect(host="localhost", user="root", password="1234", database="sample_project_db")
        mycursor = connection.cursor()
        query = "INSERT INTO  sign_in(email, password) VALUES (%s,%s)"
        val = (email, hashed)
        mycursor.execute(query, val)
        connection.commit()
        return jsonify({'result': result})





@app.route("/sign-in-get-all",methods=['GET'])
def sign_in_get_all():
  
    connection = mysql.connector.connect(host="localhost", user="root", password="1234", database="sample_project_db")
    mycursor = connection.cursor()
    mycursor.execute("SELECT email,password FROM sign_in")
    results= mycursor.fetchall()
    connection.commit()
    return jsonify(results)

@app.route("/sign-in-get",methods=['GET'])
def sign_in_get():
    sign_in_get_details= request.get_json()
    email = sign_in_get_details['email']
    password = sign_in_get_details['password']
  
    connection = mysql.connector.connect(host="localhost", user="root", password="1234", database="sample_project_db")
    mycursor = connection.cursor()
    sql="SELECT * FROM users Where email=%s AND password=%s "
    data_search=(email,password)
   
    mycursor.execute(sql,data_search)
    results= mycursor.fetchall()
    connection.commit()
    return jsonify({"results":results})

  
@app.route('/sign-up', methods=['POST'])
def sign_up():
    result = [{'msg': 'success'}, {'stat': '200 ok'}]
    if request.method == 'POST':
        sign_up_details= request.get_json()
        firstname = sign_up_details['firstname']
        lastname = sign_up_details['lastname']
        email = sign_up_details['email']
        password = sign_up_details['password']

        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
      
        connection = mysql.connector.connect(host="localhost", user="root", password="1234", database="sample_project_db")
        mycursor = connection.cursor()
        query = "INSERT INTO  users(first_name,last_name,email, password) VALUES (%s,%s,%s,%s)"
        val = (firstname, lastname,email, hashed)
        mycursor.execute(query, val)
        connection.commit()
        return jsonify({'result': result})


@app.route("/sign-up-get",methods=['GET'])
def sign_up_get():
    try:
        connection = mysql.connector.connect(host='localhost',database='sample_project_db',user='root',password='1234')
        sql_select_Query = "select * from users"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        return jsonify({'records': records})
            
    except Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if (connection.is_connected()):
            connection.close()
            cursor.close()
            print("MySQL connection is closed")

@app.route('/address', methods=['POST'])
def address():
    result = [{'msg': 'success'}, {'stat': '200 ok'}]
    if request.method == 'POST':
        address_details= request.get_json()
        line1 = address_details['line1']
        line2 = address_details['line2']
        postalcode = address_details['postalcode']
        city = address_details['city']
        state = address_details['state']
        country = address_details['country']
      
        connection = mysql.connector.connect(host="localhost", user="root", password="1234", database="sample_project_db")
        mycursor = connection.cursor()
        query = "INSERT INTO  address(line1,line2,postal_code,city,state,country) VALUES (%s,%s,%s,%s,%s,%s)"
        val = (line1,line2,postalcode,city, state, country)
        mycursor.execute(query, val)
        connection.commit()
        return jsonify({'result': result})

@app.route("/address-get",methods=['GET'])
def address_get():
    try:
        connection = mysql.connector.connect(host='localhost',database='sample_project_db',user='root',password='1234')
        sql_select_Query = "select * from address"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        return jsonify({'records': records})
            
    except Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if (connection.is_connected()):
            connection.close()
            cursor.close()
            print("MySQL connection is closed")

@app.route('/business', methods=['POST'])
def business():
    result = [{'msg': 'success'}, {'stat': '200 ok'}]
    if request.method == 'POST':
        business_details= request.get_json()
        businessname = business_details['businessname']
        businessownername = business_details['businessownername']
        businessregno = business_details['businessregno']
        contactno = business_details['contactno']
        
      
        connection = mysql.connector.connect(host="localhost", user="root", password="1234", database="sample_project_db")
        mycursor = connection.cursor()
        query = "INSERT INTO  business(business_name,business_owner_name,business_reg_no,contact_no) VALUES (%s,%s,%s,%s)"
        val = (businessname,businessownername,businessregno,contactno)
        mycursor.execute(query, val)
        connection.commit()
        return jsonify({'result': result})

@app.route("/business-get",methods=['GET'])
def business_get():
    try:
        connection = mysql.connector.connect(host='localhost',database='sample_project_db',user='root',password='1234')
        sql_select_Query = "select * from business"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        return jsonify({'records': records})
            
    except Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if (connection.is_connected()):
            connection.close()
            cursor.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    app.run(debug=True)