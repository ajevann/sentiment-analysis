#!/usr/bin/python

import MySQLdb
import csv

# Open database connection
#db = MySQLdb.connect("localhost","root","password","sentimentanalysis")
#db = MySQLdb.connect(host="localhost",user="root",passwd="password",db="sentimentanalysis", port=3306)
db = MySQLdb.connect(host="localhost",user="root",passwd="password",db="sentimentanalysis", port=8889)

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.

with open('train.tsv','rb') as tsvin:
    tsvin = csv.reader(tsvin, delimiter='\t')

    for row in tsvin:
		sql = "INSERT INTO phrases(phraseid, sentenceid, phrase, sentiment, sentimentdouble) VALUES (" + row[0] + ", " + row[1] + ", '" + row[2] + "', " + row[3] + ", " + row[3] + ")"
		try:
		   # Execute the SQL command
		   cursor.execute(sql)
		   print(sql)
		   # Commit your changes in the database
		   db.commit()
		except:
		   # Rollback in case there is any error
		   db.rollback()

# disconnect from server
db.close()