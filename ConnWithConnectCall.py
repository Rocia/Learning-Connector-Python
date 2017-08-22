import mysql.connector

cnx = mysql.connector.connect(user='root', password='root@123',
                              host='localhost',
                              database='citation',
                              use_pure=False)
cnx.close()