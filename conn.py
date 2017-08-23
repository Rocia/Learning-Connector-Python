#creating connection object
#note this can also be done using MySQLdb howevr due to support issueas for python3 this is the prefered option for python3 and higher
import mysql.connector

cnx = mysql.connector.connect(user='root', password='root@123', host='localhost', database='Test')
cnx.close()