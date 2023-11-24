import pymongo
import requests
client=pymongo.MongoClient()
db=client['node']
col=db['product']
resp=requests.get('https://dummyjson.com/products')
p_dict=resp.json()
p_list=p_dict["products"]
list=[]

for product in p_list:
    list.append({"name": product['title'], "price": product['price'],"brand": product['brand'], "stock": product['stock'], "avail": True})
col.insert_many(list)