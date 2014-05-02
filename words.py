#!/usr/bin/python

import MySQLdb
import csv

# Open database connection
#db = MySQLdb.connect("localhost","root","password","sentimentanalysis")
db = MySQLdb.connect(host="localhost",user="root",passwd="password",db="sentimentanalysis", port=3306)
#db = MySQLdb.connect(host="localhost",user="root",passwd="password",db="sentimentanalysis", port=8889)

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = "SELECT phrase_lower, sentiment FROM phrases_train WHERE word_count = 1 "

try:
	# Execute the SQL command
	cursor.execute(sql)
	# Fetch all the rows in a list of lists.
	results = cursor.fetchall()
	for row in results:
		word = str(row[0]).replace('\'', '\\\'')
		sql = "INSERT INTO words(word, sentiment, sentiment_double) VALUES (\'" + word + "\', " + str(row[1]) + ", " + str(row[1]) + ")"
		try:
			cursor.execute(sql)
			# Commit your changes in the database
			db.commit()
		except MySQLdb.Error, e:
			print("\n" + sql)
			print "An error has been passed. %s" %e
			# Rollback in case there is any error
			db.rollback()
except MySQLdb.Error, e:
	print "An error has been passed. %s" %e
	# Rollback in case there is any error
	db.rollback()

# disconnect from server
db.close()
