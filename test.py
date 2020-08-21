import sqlite3

connection =sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users(id int,username text,password text )"
cursor.execute(create_table)

user =(1,'john','smith')
insert_query="INSERT INTO users VALUES (?,?,?)"
cursor.execute(insert_query,user)

users =[

(2,'mike','white'),
(3,'bob','dilan')
]
cursor.executemany(insert_query, users)

selected_query ="SELECT * FROM users"

for row in cursor.execute(selected_query):
    print(row)


connection.commit()
connection.close()