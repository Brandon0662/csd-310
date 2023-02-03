from pymongo import MongoClient

url = "mongodb+srv://admin:admin@atlascluster.ztpyedf.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

print("\n -- Pytech COllection List --")
print(db.list_collection_names())

# show an exit message
input("\n\n  End of program, press any key to exit... ")