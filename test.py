#!/usr/bin/python

import MySQLdb
import csv

# Open database connection
#db = MySQLdb.connect("localhost","root","password","sentimentanalysis")
db = MySQLdb.connect(host="localhost",user="root",passwd="password",db="sentimentanalysis", port=3306)
#db = MySQLdb.connect(host="localhost",user="root",passwd="password",db="sentimentanalysis", port=8889)

# prepare a cursor object using cursor() method
cursor = db.cursor()

row = [5, "blah", 8]


try:
	# Execute the SQL command
	sql = "INSERT INTO words(word, sentiment) VALUES (\'" + row[1] + "\', " + str(row[0]) + ")"
	print(sql)
	cursor.execute(sql)
	# Commit your changes in the database
	db.commit()
except:
	# Rollback in case there is any error
	print("error")
	db.rollback()

# disconnect from server
db.close()