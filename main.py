import pymongo

client = pymongo.MongoClient("mongodb+srv://miqbalatif:<9m405Q1bzYdoHvhR>@cluster0.f5drkp0.mongodb.net/?retryWrites=true&w=majority")
db = client.test
d={ "name": "MiqbalAtif", "age": "21", "address": "Jakarta", "hobby": "Programming"}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)

print (db)