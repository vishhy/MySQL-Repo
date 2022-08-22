# Storing dressdetails.json in mongo db

import pymongo as pm
import logging as lg
import json

connection = pm.MongoClient("mongodb+srv://vishwas:hJqP4-ef65@cluster-vishwas.v3i9doq.mongodb.net/?retryWrites=true&w"
                            "=majority")
db = connection.test

lg.basicConfig(filename='log1.log', level=lg.INFO, format='%(asctime)s %(name)s %(levelname)s %(message)s\n')

try:
    database = connection['Dresses']
    lg.info(msg='Database created successfully')
    collection = database['Dress Details']
    lg.info(msg='Collection created successfully')
except Exception as e:
    collection = connection['mongotest']['test_dress']
    lg.error(e)

# Loading JSON file
try:
    with open(r"F:\FSDS\Pandas Class Notes\data fsds\dressdetails.json") as json_file:
        file_data = json.load(json_file)
        lg.info(msg='JSON file loaded successfully')
except Exception as e:
    lg.error(e)

# Inserting data in mongo db
if isinstance(file_data, list):
    collection.insert_many(file_data)
    lg.info(msg='Records have been uploaded successfully in Mongo DB')
else:
    collection.insert_one(file_data)
    lg.info(msg='Records have been uploaded successfully in Mongo DB')