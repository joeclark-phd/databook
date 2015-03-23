#!venv/bin/python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return( "Hello World! This is Flask." )
    
@app.route("/profiles", methods=['GET'])
def profiles():
    return( "List of profiles" )
    
@app.route("/profile/<string:id>", methods=['GET'])
def get_profile(id):
    return( "Profile " + id + " details" )
    
@app.route("/profiles", methods=['POST'])
def post_profile():
    return( "Creating new profile" )
    
@app.route("/profile/<string:id>", methods=['PUT'])
def update_profile(id):
    return( "Updating profile " + id )
    
@app.route("/profile/<string:id>", methods=['DELETE'])
def delete_profile(id):
    return( "Deleting profile " + id )
    
@app.route("/companies")
def companies():
    return( "List of companies" )
    
@app.route("/company/<string:id>/profiles")
def company_profiles(id):
    return( "List of users who worked for company " + id )
    
if __name__ == '__main__':
    app.run(debug=True)
