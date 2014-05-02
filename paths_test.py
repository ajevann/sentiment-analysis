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
		print(phrase[0])
		for word in phrase[0].split(' '):
			sql = "SELECT word, sentiment from words where word = \'" + word.replace('\'', '\\\'') + "\'"

			cursor.execute(sql)
			matches = cursor.fetchall()

			print(word + " " + str(matches[0][1]))


	# Commit your changes in the database
	#db.commit()

except MySQLdb.Error, e:
	print "An error has been passed. %s" %e
	print("[ " + sql + " ]")
	# Rollback in case there is any error
	db.rollback()

# disconnect from server
db.close()