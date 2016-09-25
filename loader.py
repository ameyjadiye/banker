#!/usr/bin/python

'''
    File name: loader.py
    Author: Amey Jadiye
    Date created: 25/9/2016
    Python Version: 2.7
    Desc: For loading HDFC dump file in to database
'''


import MySQLdb
import sys

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="9",  # your password
                     db="banks")        # name of the data base

tran_f = open(sys.argv[1],'r');

#  you execute all the queries you need
cur = db.cursor()

count=1
for line in tran_f:
	row=line.strip().split(',')
	date=row[0].strip()
	reference=row[1].strip()
	value_date=row[2].strip()
	debit_amount=row[3].strip()
	credit_amount=row[4].strip()
	ref_number=row[5].strip()
	closing_balance=row[6].strip()

	# Use all the SQL you like
	sql="insert into  transactions(bank,date,reference,value_date,debit_amount,credit_amount,ref_number,closing_balance) values ('HDFC',STR_TO_DATE(\'"+date+"\', \'%d/%m/%yy\'),\'"+reference+"\',STR_TO_DATE(\'"+value_date+"\', \'%d/%m/%yy\'),"+debit_amount+","+credit_amount+",\'"+ref_number+"\',"+closing_balance+")"
	
	try:
	 
		cur.execute(sql)
		db.commit()
	except Exception as e:
		print str(count) + sql
		print e

	count=count+1

db.close()
tran_f.close()
