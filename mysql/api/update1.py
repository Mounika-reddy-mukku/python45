import mysql.connector
import requests
mydb=None
mycursor=None
try:
    mydb=mysql.connector.connect(host="localhost", user="root", password="Root", database="employee")
    mycursor=mydb.cursor()
    sql_up='''insert into user1(eid,ename,gender) values(%s,%s,%s)'''
    response=requests.get('https://dummyjson.com/users')
    print(type(response))
    emp_dict=response.json()
    print(type(emp_dict))
    emp_list = emp_dict["users"]
    data = []
    for emp in emp_list:
        data.append((emp['id'], emp['firstName'], emp['gender']))
    mycursor.executemany(sql_up,data)
    mydb.commit()
    print("Data using API inserted successfully")
    
except mysql.connector.DatabaseError as err:
    if(err):
        print(err)
finally:
    mycursor.close()
    mydb.close()