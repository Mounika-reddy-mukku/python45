import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root", password='Root', database="employee")
mycursor=mydb.cursor()
sql_create='''create table user1(eid int, ename varchar(32), gender varchar(32))'''
mycursor.execute(sql_create)
mydb.commit()
mycursor.close()
mydb.close()
