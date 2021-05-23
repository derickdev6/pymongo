import pymongo
client = pymongo.MongoClient("localhost", 27017)
db = client.myblog
print(db.name)

username = input("UserName: ")
userage = int(input("UserAge: "))
db.users.insert_one({"name": username, "age": userage}).inserted_id
# print(db.users.find())
