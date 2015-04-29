#! /usr/bin/env python
# -*- coding: iso-8859-15 -*-

import sys, csv, sqlite3

con = sqlite3.connect("sendatabase.sqlite")

cur = con.cursor()

cur.execute(" DROP TABLE IF EXISTS INFORMATION;")
cur.execute(" CREATE TABLE INFORMATION (NAME VARCHAR NOT NULL, CORES INTEGER NOT NULL, MEMORY NUMERIC NOT NULL, COST NUMERIC NOT NULL, PROVIDER VARCHAR NOT NULL);")

with open("all_data.csv", "rb") as f:
	reader = csv.reader(f, delimiter=',')

	for row in reader:
		to_db = [unicode(row[3], "utf8"), unicode(row[1], "utf8"), unicode(row[0], "utf8"), unicode(row[2], "utf8"), unicode(row[4], "utf8")]
		cur.execute("INSERT INTO INFORMATION (NAME, CORES, MEMORY, COST, PROVIDER) VALUES(?, ?, ?, ?, ?);", to_db)
		con.commit()

con.close()