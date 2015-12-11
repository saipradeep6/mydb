#!/usr/bin/python

import MySQLdb as mdb

# prepare a cursor object using cursor() method

db = mdb.connect('localhost', 'root', 'Purple@123', 'saltdb')
cursor = db.cursor()
cursor.execute("SELECT * FROM saltdata")
results = cursor.fetchall()
for row in results:
        id = row[0]
        firstname = row[1]
        lastname = row[2]
        email = row[3]
        reg_date = row[4]
        print "id=%d, firstname=%s, lastname=%s, email=%s, reg_date=%s" % \
             (id, firstname, lastname, email, reg_date)
cursor.close()
db.close()
