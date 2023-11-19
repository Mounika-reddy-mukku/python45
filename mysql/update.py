import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root", password="Root", database="employee")
mycursor=mydb.cursor()
sql_up='''insert into emp values(102,"Vakula", 60000)'''
mycursor.execute(sql_up)
mydb.commit()
mycursor.close()
mydb.close()