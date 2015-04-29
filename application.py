#! /usr/bin/env python
# -*- coding: iso-8859-15 -*-

import sys, sqlite3, getopt

con = sqlite3.connect("sendatabase.sqlite")

cur = con.cursor()

precio = ""
cores = ""
memoria = ""

try:
	opts, args = getopt.getopt(sys.argv[1:], "p:c:m:", ["price=", "cores=", "memory="])
except getopt.GetoptError:
	usage()
	sys.exit(2)
for opt, arg in opts:
	if opt in ("-p", "--price"):
		precio = arg
	elif opt in ("-c", "--cores"):
		cores = arg
	elif opt in ("-m", "--memory"):
		memoria = arg

query = "SELECT * FROM INFORMATION WHERE "


if (len(memoria) > 0) and (len(cores) > 0):
	query += "MEMORY >= " + str(memoria) + " AND CORES >= " + str(cores) + " ORDER BY COST;"
elif (len(memoria) == 0) and (len(cores) > 0):
	query += "CORES >= " + str(cores) + " ORDER BY COST;"
elif (len(memoria) > 0) and (len(cores) == 0):
	query += "MEMORY >= " + str(memoria) + " ORDER BY COST;"
elif (len(memoria) > 0) and (len(precio) > 0) and (len(cores) > 0):
	print "QUERY NOT SUPPORTED"
elif (len(memoria) == 0) and (len(precio) == 0) and  (len(cores) == 0):
	query = "SELECT * FROM INFORMATION ORDER BY COST;"
elif (len(memoria) == 0) and (len(precio) > 0) and (len(cores) == 0):
	query += "COST <= " + str(precio) + " ORDER BY COST;"

cur.execute(query)

for row in cur:
	print " PROVIDER: %7s | NAME: %15s | CORES: %3d | MEMORY (GB): %3d | COST (US$ p.h.): %6.3f" % (row[4], row[0], row[1], row[2], row[3])

con.close()