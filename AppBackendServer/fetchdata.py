#!/usr/bin/python
# view_rows.py - Fetch and display the rows from a MySQL database query

# import the MySQLdb and sys modules
import MySQLdb
import sys
import json
import collections

# open a database connection
# be sure to change the host IP address, username, password and database name to match your own
connection = MySQLdb.connect (host = "localhost", user = "root", password = "", db = "restapirobi")

# prepare a cursor object using cursor() method
cursor = connection.cursor ()

# execute the SQL query using execute() method.
cursor.execute ("select * from appbackendapi_promotionad")

# fetch all of the rows from the query
data = cursor.fetchall ()
user_list = []

# print the rows
for row in data :
  d=collections.OrderedDict()
  d['firstName']  = row[1] #name
  d['lastName']   = row[2] #lname
  d['email']      = row[3] #email
  user_list.append(d)
  
print(json.dumps(user_list))

# close the cursor object
cursor.close ()

# close the connection
connection.close ()

# exit the program
sys.exit()