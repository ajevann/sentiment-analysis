#!/usr/bin/python

import MySQLdb
import csv

# Open database connection
db = MySQLdb.connect("localhost","root","password","sentimentanalysis" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "INSERT INTO phrases(phraseid, sentenceid, phrase, sentiment, sentimentdouble) VALUES (123, 321, 'blah blah blah', 2, 2)"
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()