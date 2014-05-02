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
	sql = "SELECT phrase, phrase_id from phrases_test where word_count = 1 and sentiment IS NULL"
	
	cursor.execute(sql)
	results = cursor.fetchall()

	count = 0;

	for phrase in results:
		for word in phrase[0].split(' '):
			sql = "SELECT word, sentiment from words where word = \'" + word.replace('\'', '\\\'') + "\'"
			#print(sql)
			cursor.execute(sql)
			matches = cursor.fetchall()

			#if count % 100 == 0:
			#	print(count) 

			if len(matches) != 0:
				print(matches)
			#	count += 1
				sql = "UPDATE phrases_test set sentiment = " + str(matches[0]) + " where phrase = \'" + word.replace('\'', '\\\'') + "\'"
				#print(str(matches[0]) + " " + word)
				#cursor.execute(sql)


	# Commit your changes in the database
	# db.commit()

except MySQLdb.Error, e:
	print "An error has been passed. %s" %e
	print("[ " + sql + " ]")
	# Rollback in case there is any error
	db.rollback()

# disconnect from server
db.close()