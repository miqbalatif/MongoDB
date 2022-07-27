import pymongo as pm
client = pm.MongoClient("
client = pymongo.MongoClient("mongodb+srv://miqbalatif:<Fozia@5170641>@cluster0.z6knzi2.mongodb.net/?retryWrites=true&w=majority")
db = client.test
")
db = client.test
print(db)
# d={'name':'ali', 'age':20, 'job':'student', 'marital':'single', 'education':'highschool'}
# d1={'name':'ali', 'age':20, 'job':'student', 'marital':'single', 'education':'highschool'}
# d2={'name':'ali', 'age':20, 'job':'student', 'marital':'single', 'education':'highschool'}
# d3={'name':'ali', 'age':20, 'job':'student', 'marital':'single', 'education':'highschool'}
# d4={'name':'ali', 'age':20, 'job':'student', 'marital':'single', 'education':'highschool'}
# db1 = client['mongotest']
# coll = db1['test']
# coll.insert_one(d)