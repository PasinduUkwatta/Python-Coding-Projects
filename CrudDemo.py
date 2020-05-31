from pymongo import MongoClient
from pymongo import version
from pprint import pprint

print(version)

client = MongoClient(port=27017)

db =client.Northwind.catagories

print('the total number of documents in northwind is')

total_doc = db.Northwind.catagories
pprint(total_doc)

filter_query ={"name" :"amazon\i"}
print('the total of tv in amazon')
document_amazon = db.products.find(filter_query)

for doc in document_amazon:
    pprint(doc)