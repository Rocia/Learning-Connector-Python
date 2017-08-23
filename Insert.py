from __future__ import print_function
import mysql.connector

cnx = mysql.connector.connect(user='root', password='root@123', host='localhost', database='citation')
cursor = cnx.cursor()


add_employee = ("INSERT INTO `cite`(`ID`, `USER`, `DATE`, `PVP`, `LINK`, `UNQ`, `YEAR`, `STATUS`) VALUES ([value-1],[value-2],[value-3],[value-4],[value-5],[value-6],[value-7],[value-8])")

# Insert new employee
cursor.execute(add_employee)

cnx.commit()

cursor.close()
cnx.close()