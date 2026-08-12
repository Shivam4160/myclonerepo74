from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db=client["db"]
collection = db["invoices"]
#collection.insert_one({"name":"shivam","Age":20,"phone":9876543210})
#collection.insert_many([{"name":"ram","Age":20,"phone":9876543211},{"name":"raj","Age":21,"phone":9876543212},{"name":"raghu","Age":21,"phone":9876543213}])
invoices=collection.find()

for data in invoices:
    for key , value in list(data.items())[1:]:
        print(f"{key}:{value}")
    print("")
#print(invoices)
