import pymongo
client=pymongo.MongoClient()
db=client['node']
col=db['employee']
users=col.find({})
for user in users:
    print(user['first_name'], user['gender'])
print(type(user))

