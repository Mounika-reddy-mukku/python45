import mysql.connector
mydb=None
mycursor=None
try:
    mydb=mysql.connector.connect(host="localhost", user="root", password="Root", database="employee")
    mycursor=mydb.cursor()
    my_up='''insert into user(uid,uname,ucity) values(%s,%s,%s)'''
    data= [(101, "Nandu", "Bangalore"), (102,"Pinky", "Hyderabad")]
    mycursor.executemany(my_up,data)
    mydb.commit()
    print("data inserted successfully")
except mysql.connector.DatabaseError as err:
    if(err):
        print(err)
finally:
    mycursor.close()
    mydb.close()
    