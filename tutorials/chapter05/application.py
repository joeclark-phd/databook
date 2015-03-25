#!venv/bin/python
from flask import Flask, abort, request
from pymongo import MongoClient
from bson import json_util

application = Flask(__name__)

# (USE YOUR CONNECTION DETAILS FROM MONGOLAB)
MONGO_URL = 'mongodb://<uname>:<pass>@<database URL>'

# connect to the mongoDB server
client = MongoClient(MONGO_URL) 

# connect to the default database 
db = client.get_default_database()



@application.route("/")
def index():
    return( "Hello World! This is Flask." )
    
@application.route("/profiles", methods=['GET'])
def profiles():
    # run a query -- find all profiles
    data = db.profiles.find()
    # turn the data into human-readable JSON
    return( json_util.dumps({"profiles":data})  )
    
@application.route("/profile/<string:id>", methods=['GET'])
def get_profile(id):
    data = db.profiles.find_one({"_id":id})
    return( json_util.dumps(data) )
    
@application.route("/profiles", methods=['POST'])
def post_profile():
    if not request.json:
        abort(400) # 400 error = bad request
    response = db.profiles.insert(request.json)
    return( response )
        
@application.route("/profile/<string:id>", methods=['PUT'])
def update_profile(id):
    if not request.json:
        abort(400)
    response = db.profiles.update({"_id":id},request.json)
    return( response )
    
@application.route("/profile/<string:id>", methods=['DELETE'])
def delete_profile(id):
    response = db.profiles.remove({"_id":id})
    return( response )
    
@application.route("/companies")
def companies():
    return( "List of companies" )
    
@application.route("/company/<string:id>/profiles")
def company_profiles(id):
    return( "List of users who worked for company " + id )
    
if __name__ == '__main__':
    application.run(debug=True)
