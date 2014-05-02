#!/usr/bin/python

import MySQLdb
import csv

# Open database connection
#db = MySQLdb.connect("localhost","root","password","sentimentanalysis")
db = MySQLdb.connect(host="localhost",user="root",passwd="password",db="sentimentanalysis", port=3306)
#db = MySQLdb.connect(host="localhost",user="root",passwd="password",db="sentimentanalysis", port=8889)

sql = ""

# prepare a cursor object using cursor() method
cursor = db.cursor()

try:
	# Execute the SQL command
	sql = "SELECT phrase, phrase_id from phrases_test"
	
	cursor.execute(sql)
	results = cursor.fetchall()

	for phrase in results:
		sql = "SELECT phrase, sentiment from phrases_train where phrase = \'" + phrase[0].replace('\'', '\\\'') + "\'"

		cursor.execute(sql)
		matches = cursor.fetchall()

		if phrase[1] % 1000 == 0:
			print(str(phrase[1]) + " : " + phrase[0]) 

		if len(matches) != 0:
			matches = matches[0]
			#print(str(phrase[1]) + " : " + str(matches[1]) + " ... " + matches[0])

			sql = "UPDATE phrases_test SET sentiment  = " + str(matches[1]) + " where phrase_id = " + str(phrase[1])
			cursor.execute(sql)

		#print(str(phrase[1]) + " " + phrase[0])

	# Commit your changes in the database
	db.commit()

except MySQLdb.Error, e:
	print "An error has been passed. %s" %e
	print("[ " + sql + " ]")
	# Rollback in case there is any error
	db.rollback()

# disconnect from server
db.close()