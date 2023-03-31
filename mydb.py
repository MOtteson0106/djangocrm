import mysql.connector

database = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'damnit77'
	)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE ottoco")

print("All done!")
