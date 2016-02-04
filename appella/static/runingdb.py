#!/usr/bin/python
import psycopg2, pyproj, sys
from os import system
from math import sin,cos,sqrt,asin,pi

def main():
	conn_string = "host='127.0.0.1' dbname='dbella' user='ella' password='ella'"

	conn = psycopg2.connect(conn_string)
	print "Connecting to database\n	->%s" % (conn_string)

	cursor = conn.cursor()
	y1 = -17.280216551959015
	y2 = -17.84582099396257
	x2 = -65.88346355078124
	x1 = -66.43812312109372
	while y1 > y2:
		longitud = x1
		while x2 > x1:
			lat1 = y2
			lon1 = x1
			lat2 = y2
			lon2 = x1 + 0.004
			lat3 = y2 + 0.004
			lon3 = x1
			lat4 = y2 + 0.004
			lon4 = x1 + 0.004
			cursor.execute("INSERT INTO appella_area(ar_lat1, ar_lon1, ar_lat2, ar_lon2, ar_lat3, ar_lon3, ar_lat4, ar_lon4) VALUES('"+str(lat1)+"', '"+str(lon1)+"', '"+str(lat2)+"', '"+str(lon2)+"', '"+str(lat3)+"', '"+str(lon3)+"', '"+str(lat4)+"', '"+str(lon4)+"');");
			x1 += 0.004
		x1 = longitud
		y2 += 0.004
	conn.commit()
	print "Records created successfully";
	conn.close()

if __name__ == "__main__":
	main()

