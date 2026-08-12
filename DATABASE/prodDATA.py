from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db=client["tybsc"]
collection = db["student"]

#prodect_data = ([{"name":"shivam","price":200,"item":'ball'},{"name":"raj","price":150,"item":'cover'},{"name":"raghu","price":750,"item":'light'}])
#collection.insert_many(prodect_data)

datas = collection.find()

for data in datas:
    for key , value in list(data.items())[1:]:
        print(f"{key}:{value}")
    print("")
'''
collection.update_many({"name":"raj"},{"$set":{"item":"book"}})
print("__________________________________________")
datas = collection.find()
for data in datas:
    for key , value in list(data.items())[1:]:
        print(f"{key}:{value}")
    print("")

collection.delete_one({"name":"raghu"})

datas = collection.find()
for data in datas:
    for key , value in list(data.items())[1:]:
        print(f"{key}:{value}")
    print("")
    
'''
