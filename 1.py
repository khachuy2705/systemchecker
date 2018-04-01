#!/usr/bin/python
import mysql.connector
cnx = mysql.connector.connect(user='redmine', password='password',
	host='127.0.0.1',
	database='redmine')
try:
	cursor = cnx.cursor()
	cursor.execute("""
		select * from users
		""")
	result = cursor.fetchall()
	f=open('data', 'wb')
	for row in result:
		for field in row:
			f.write(field)
			f.write(b',')
			f.write(b'\n')
#	print result
finally:
	cnx.close()