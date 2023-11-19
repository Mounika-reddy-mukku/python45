import pymongo
client=pymongo.MongoClient()
db=client['usersDatabase']
col=db['users']
