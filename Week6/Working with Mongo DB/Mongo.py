import pymongo

# It is document database

uri = "mongodb+srv://shreyashsingh1:Lookinto1234@cluster0.cihs6do.mongodb.net/"

# initializes a connection to a MongoDB database using the PyMongo library in Python.
# MongoClient It is a class provided by the PyMongo library that represents a connection to a MongoDB server.

"""
By passing the uri to the MongoClient constructor, a new instance of the MongoClient class is created, 
establishing a connection to the MongoDB server specified in the URI. The client variable then holds this instance, 
which can be used to interact with the database.
"""

client = pymongo.MongoClient(uri)

"""db = client.test: This line assigns the test database to the db variable. 
The test database is a common default database used for testing and experimentation. 
You can replace test with the name of the specific database you want to work with.
After executing these lines, you can perform various operations on the db object,
such as creating collections, inserting documents, querying data, and more."""

# db = client.test
db = client["testdb1"]
print(db)

data = {
    "Name": "Shreyash",
    "Class": "DSM",
    "Date": "Flexi"
}

data1 = {
    "Email": "shreyashsingh865@gmail.com",
    "Address": "Andheri"
}

data2 = [
    {"name": "Amy", "address": "Apple st 652"},
    {"name": "Hannah", "address": "Mountain 21"},
    {"name": "Michael", "address": "Valley 345"},
    {"name": "Sandy", "address": "Ocean blvd 2"},
    {"name": "Betty", "address": "Green Grass 1"},
    {"name": "Richard", "address": "Sky st 331"},
    {"name": "Susan", "address": "One way 98"},
    {"name": "Vicky", "address": "Yellow Garden 2"},
    {"name": "Ben", "address": "Park Lane 38"},
    {"name": "William", "address": "Central st 954"},
    {"name": "Chuck", "address": "Main Road 989"},
    {"name": "Viola", "address": "Sideway 1633"}
]

data3 = {
    "name": "notebook",
    "qty": 50,
    "rating": [{"score": 8}, {"score": 9}],
    "size": {"height": 11, "width": 8.5, "unit": "in"},
    "status": "A",
    "tags": ["college-ruled", "perforated"]
}

random_data = [
    {'_id': '3', 'companyName': 'iNeuron', 'Faculty': 'XYZ'},
    {'_id': '4', 'companyName': 'iNeuron', 'Faculty': 'ABC'},
    {'_id': '5', 'companyName': 'iNeuron', 'Faculty': 'PQR'},
]

"""Creating Collection"""
coll_testdb1 = db["my_record"]

"""Inserting Data in collection"""
coll_testdb1.insert_one(data1)

print(coll_testdb1.insert_many(random_data))

coll_testdb1.insert_one(data3)

"""Retrieving data from DB"""
print(coll_testdb1.find_one())

"""For all record"""
# print(coll_testdb1.find())
for i in coll_testdb1.find():
    print(i)

"""Fliteration"""
for iy in coll_testdb1.find({"Name": "Shreyash"}):
    print(iy)

# -> $gte = greater than equal to
for iy in coll_testdb1.find({"_id": {"$gte": "4"}}):
    print(iy)

"""Updation of value"""
coll_testdb1.update_many({"companyName": "iNeuron"}, {"$set": {"companyName": "PWSKILLS"}})

"""Dropping the collection"""
coll_testdb1.drop()

client.close()
