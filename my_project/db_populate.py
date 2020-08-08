import sqlite3
db_locale ='users.db'

connie= sqlite3.connect(db_locale)
c=connie.cursor()

c.execute("""
	INSERT INTO comments(title,name,comments)
	VALUES ('Life Meaning','Pasindu','Always you need to Learn')			
	""")
	


connie.commit()
connie.close()
