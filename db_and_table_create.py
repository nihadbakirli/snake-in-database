import mysql.connector
import os
#def connect():
db_server_host=input(str("Enter database server hostname or ipaddress: "))
db_user=input(str("Enter database user: "))
db_passwd=input(str("Enter password: "))
my_database=input(str("Enter database name: "))
#mydb = null
def connect(db_server_host,db_user,db_passwd,my_database):
	return mysql.connector.connect(
		host=(db_server_host),
		user=(db_user),
		password=(db_passwd),
		database=(my_database)
	)
mydb = connect(db_server_host,db_user,db_passwd,my_database)
while True:
	print("1) CREATE USER")
	print("2) SHOW USER ")
	print("3) EXIT FROM SCRIPT")
	answer=input(str("CHOSE YOUR NUMBER: "))
	if answer == "1":
		username = input(str("Enter username: "))
		pass_word = input(str("Set user password: "))
		user_id = input("Enter user id: ")
		os.system("useradd -u {} {}".format(user_id,username))
		os.system("echo {} | passwd {} --stdin".format(pass_word,username))
		myinsert = mydb.cursor()
		sql = "INSERT INTO info (id, name, password) VALUES (%s, %s, %s)"
		val = (user_id, username, pass_word)
		myinsert.execute(sql, val)
		mydb.commit()
		print(myinsert.rowcount, "record inserted.")
		break
	elif answer == "2":
		myselect = mydb.cursor()
		myselect.execute("SELECT * FROM info")
		for i in myselect:
			print(i)
		break
	elif answer == "3":
		break
	else:
		print("Please choose correct varian")

print("Finish")
