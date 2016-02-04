#!/usr/bin/python
import psycopg2, pyproj, sys
from os import system
from math import sin,cos,sqrt,asin,pi

'''
cbbax1y1---------------cbbax2y2
|			y1				|
|			Cbba			|
|	x2				x1		|
|			y2				|
cbbax3y3---------------cbbax4y4
'''

def main():
	conn_string = "host='127.0.0.1' dbname='dbella' user='ella' password='ella'"

	conn = psycopg2.connect(conn_string)
	print "Connecting to database\n	->%s" % (conn_string)

	cursor = conn.cursor()
#	x = [-17.375121527147712, -66.16868132184294]
#	y = [-17.3745454, -66.16619779999996]
#	La distancia es: 271.53247815762677
#	x = [-17.384295692326056, -66.19597548077849]
#	y = [-17.3745454, -66.16619779999996]
#	La distancia es: 3344.5268500305015
	cbbax1 = -66.43812312109372
	cbbay1 = -17.280216551959015
	cbbax2 = -65.88346355078124
	cbbay2 = -17.280216551959015
	cbbax3 = -66.43812312109372
	cbbay3 = -17.84582099396257
	cbbax4 = -65.88346355078124
	cbbay4 = -17.84582099396257
	linea = True
#(-17.280216551959015+17.84582099396257)/2+17.280216551959015
#(65.88346355078124-66.43812312109372)/2+65.88346355078124
	y1 = -17.280216551959015
	y2 = -17.84582099396257
	x2 = -65.88346355078124
	x1 = -66.43812312109372
	salto = 1
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
#			print str(lat1)+',',str(lon1)+',',str(lat2)+',',str(lon2)+',',str(lat3)+',',str(lon3)+',',str(lat4)+',',str(lon4)+','
			cursor.execute("INSERT INTO appella_area(ar_lat1, ar_lon1, ar_lat2, ar_lon2, ar_lat3, ar_lon3, ar_lat4, ar_lon4) VALUES('"+str(lat1)+"', '"+str(lon1)+"', '"+str(lat2)+"', '"+str(lon2)+"', '"+str(lat3)+"', '"+str(lon3)+"', '"+str(lat4)+"', '"+str(lon4)+"');");
			x1 += 0.004
			salto += 1
		x1 = longitud
#		print '\n'
		y2 += 0.004
	print salto

	conn.commit()
	print "Records created successfully";
	conn.close()

if __name__ == "__main__":
	main()

#	x = [-17.375121527147712, -66.16868132184294]
#	y = [-17.3745454, -66.16619779999996]
#	La distancia es: 271.53247815762677
#x = [-17.384295692326056, -66.19597548077849]
#y = [-17.3745454, -66.16619779999996]
#	La distancia es: 3344.5268500305015
'''
x = [-17.280216551959015, -66.43712355109372]
y = [-17.280216551959015, -66.43312355078124]
#	La distancia es: 58977.28
system("clear")
 
print "Elija la opcion del elipsoide"
 
print "WGS84 = 1 GRS80 = 2 clrk66 = 3 intl = 4"
     
opcion = int(raw_input("opcion = ? "))
 
lat1 = x[0]
long1 = x[1]
lat2 = y[0]
long2 = y[1]
 
if opcion == 1:
    name_ellps = "WGS84"
 
elif opcion == 2:
    name_ellps = "GRS80"
 
elif opcion == 3:
    name_ellps = "clrk66"
 
elif opcion == 4:
    name_ellps = "intl"
 
else:
    print "No existe la opcion"
    sys.exit()
 
long1,lat1 = (long1,lat1)
long2,lat2 = (long2,lat2)
geod = pyproj.Geod(ellps=name_ellps)
angle1,angle2,distance = geod.inv(long1, lat1, long2, lat2)
 
print "La distancia es %0.2f metros basada en el elipsoide de" % distance, name_ellps
 
r = 6371000 #radio terrestre medio, en metros
 
c = pi/180 #constante para transformar grados en radianes
 
#Formula de haversine
d = 2*r*asin(sqrt(sin(c*(lat2-lat1)/2)**2 + cos(c*lat1)*cos(c*lat2)*sin(c*(long2-long1)/2)**2))
 
print "La distancia es %0.2f metros basada en la formula de haversine" % d
 
print "La diferencia, en valor absoluto, es %0.2f" % abs(distance-d), "metros"
 
print "La diferencia, en valor porcentual, es %0.2f" % abs((distance-d)*100/distance), "%"
'''