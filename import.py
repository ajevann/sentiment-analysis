#!/usr/bin/python

import MySQLdb
import csv

# Open database connection
#db = MySQLdb.connect("localhost","root","password","sentimentanalysis")
db = MySQLdb.connect(host="localhost",user="root",passwd="password",db="sentimentanalysis", port=3306)
#db = MySQLdb.connect(host="localhost",user="root",passwd="password",db="sentimentanalysis", port=8889)

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.

with open('train.tsv','rb') as tsvin:
    tsvin = csv.reader(tsvin, delimiter='\t')

    for row in tsvin:
		phrase = str(row[2]).replace('\'', '\\\'')
		sql = "INSERT INTO phrases_train(phrase_id, sentence_id, phrase, phrase_lower, sentiment, sentiment_double, word_count) VALUES (" + row[0] + ", " + row[1] + ", '" + phrase + "', '" + phrase.lower() + "', " + row[3] + ", " + row[3] + ", " + str(len(phrase.split())) + ")"
		try:
			# Execute the SQL command
			cursor.execute(sql)
			# Commit your changes in the database
			db.commit()
		except MySQLdb.Error, e:
			print "An error has been passed. %s" %e
			# Rollback in case there is any error
			db.rollback()

with open('test.tsv','rb') as tsvin:
    tsvin = csv.reader(tsvin, delimiter='\t')

    for row in tsvin:
		phrase = str(row[2]).replace('\'', '\\\'')
		sql = "INSERT INTO phrases_test(phrase_id, sentence_id, phrase, phrase_lower, word_count) VALUES (" + row[0] + ", " + row[1] + ", '" + phrase + "', '" + phrase.lower() + "', " + str(len(phrase.split())) + ")"
		try:
		   # Execute the SQL command
		   cursor.execute(sql)
		   # Commit your changes in the database
		   db.commit()
		except MySQLdb.Error, e:
			print "An error has been passed. %s" %e
			# Rollback in case there is any error
			db.rollback()

# disconnect from server
db.close()