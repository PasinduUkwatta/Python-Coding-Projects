import sqlite3
db_locale ='users.db'

connie= sqlite3.connect(db_locale)
c=connie.cursor()

c.execute("""
	CREATE TABLE comments
	(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name Text,
	title Text,
	comments Text

	)

	""")


connie.commit()
connie.close()
