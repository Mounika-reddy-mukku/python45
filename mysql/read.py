import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root", password='Root', database="employee")
mycursor=mydb.cursor()
mycursor.execute('select * from user1')
data=mycursor.fetchall()
for emp in data:
    print(emp)
mycursor.close()
mydb.close()
