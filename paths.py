#!/usr/bin/python

import MySQLdb
import csv

# Open database connection
#db = MySQLdb.connect("localhost","root","password","sentimentanalysis")
db = MySQLdb.connect(host="localhost",user="root",passwd="password",db="sentimentanalysis", port=3306)
#db = MySQLdb.connect(host="localhost",user="root",passwd="password",db="sentimentanalysis", port=8889)

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = "SELECT phrase_lower, word_count, phrase_id, sentiment FROM phrases_train"

try:
	# Execute the SQL command
	cursor.execute(sql)
	# Fetch all the rows in a list of lists.
	results = cursor.fetchall()

	for phrase in results:
		if phrase[2] % 1000 == 0:
			print(phrase[2])
		word_id = -1
		path = ""
		# Single words
		if phrase[1] == 1:
			sql = "SELECT id from words where word = \'" + phrase[0].replace('\'', '\\\'') + "\'"
			cursor.execute(sql)
			word_id = cursor.fetchall()
			word_id = word_id[0][0]

			sql = "INSERT INTO paths(from_id, to_id, word_id, phrase_id) VALUES (-1, -1, " + str(word_id) + ", " + str(phrase[2]) + ")"
			cursor.execute(sql)

			path = "-1 " + str(cursor.lastrowid) + " -1"
			sql = "INSERT INTO paths_main(start_id, sentiment, path) VALUES ( " + str(cursor.lastrowid) + ", " + str(phrase[3]) + ", \'" + path + "\')"
			
			cursor.execute(sql)

		else:
			last_id = -1
			path = "-1 "
			for word in phrase[0].split(' '):
				if word != '':
					sql = "SELECT id from words where word = \'" + word.replace('\'', '\\\'') + "\'"
					cursor.execute(sql)
					word_id = cursor.fetchall()
					word_id = word_id[0][0]

					sql = "INSERT INTO paths(from_id, word_id, phrase_id) VALUES ( " + str(last_id) + ", " + str(word_id) + ", " + str(phrase[2]) + ")"
					cursor.execute(sql)
					last_id = cursor.lastrowid
					path += str(last_id) + " "
			sql = "UPDATE paths SET to_id = -1 where id = " + str(last_id)
			cursor.execute(sql)

			path += " -1"
			start_id = (path.split(' '))[1]
			sql = "INSERT INTO paths_main(start_id, sentiment, path) VALUES ( " + str(cursor.lastrowid) + ", " + str(phrase[3]) + ", \'" + path + "\' )"
			cursor.execute(sql)

	sql = "SELECT * from paths"
	cursor.execute(sql)
	results = cursor.fetchall()

	for entry in results:
		from_id = str(entry[1])
		this_id = str(entry[0])

		if (from_id != -1):
			sql = "UPDATE paths SET to_id = " + this_id + " where id = " + from_id
			cursor.execute(sql)

	db.commit()

except MySQLdb.Error, e:
	print "An error has been passed. %s" %e
	print("[ " + sql + " ]")
	# Rollback in case there is any error
	db.rollback()

# disconnect from server
db.close()
