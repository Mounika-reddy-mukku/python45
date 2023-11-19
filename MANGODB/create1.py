import pymongo
client=pymongo.MongoClient()
db=client['node']
col=db['user']
user = {
  "name": "Sammy",
  "role": "Developer"
}
col.insert_one(user)
col.find_one({"name":"sammy"})