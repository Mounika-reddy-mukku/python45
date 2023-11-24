import requests
import csv
import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root", password="Root", database="employee")
mycursor=mydb.cursor()

resp=requests.get('https://dummyjson.com/products')
p_dict=resp.json()
print(type(p_dict))
p_list=p_dict["products"]
print(type(p_list))

fp=open('data.csv','w', newline='')
csv_obj=csv.writer(fp)
csv_obj.writerow(["Id", "Product", "Price", "Rating"])
for product in p_list:
    csv_obj.writerow([product['id'],product['title'],product['price'],product['rating']])
print("data entered successfully")
fp.close()

create_table='''create table product(
    Id int,
    Product varchar(32),
    Price float,
    Rating float
)'''
mycursor.execute(create_table)

fp1=open('data.csv','r')
data=csv.reader(fp1)
next(data)
for row in data:
    insert_data='''insert into product values(tuple(row))'''
    mycursor.execute(insert_data)
fp1.close()
mydb.commit()
mycursor.close()
mydb.close()
