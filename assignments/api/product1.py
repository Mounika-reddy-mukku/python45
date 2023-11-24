import requests
import json
import mysql.connector

mydb=mysql.connector.connect(host="localhost", user="root", password="Root", database="employee")
mycursor=mydb.cursor()

resp=requests.get('https://dummyjson.com/products')
p_dict=resp.json()
print(type(p_dict))
p_list=p_dict["products"]
print(type(p_list))
fp=open('data.json','w')
list=[]
for product in p_list:
    list.append({"name": product['title'], "price": product['price'],"brand": product['brand'], "stock": product['stock'], "avail": True})
json.dump(list,fp)
fp.close()

print(list)
sql_create='''create table jsonproduct2(
    name varchar(52),
    price int,
    brand varchar(32),
    stock int
)'''
mycursor.execute(sql_create)
sql_insert='''insert into jsonproduct2 values(%s,%s,%s,%s)'''
data=[]

for value in list:
    data.append((value['name'],value['price'],value['brand'],value['stock']))
print(data)
mycursor.executemany(sql_insert,data)
mydb.commit()
mycursor.close()
mydb.close()
