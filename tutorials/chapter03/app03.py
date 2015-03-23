#!venv/bin/python
from flask import Flask, jsonify, abort

app = Flask(__name__)

# sample data
users = [
    {
        'id': '123',
        'name': 'John McLane',
        'jobs': [
            {'employer':'NYPD',
             'position':'Lieutenant',
             'start':'1988'}
        ]
    },
    {
        'id': '456',
        'name': 'James Edwards',
        'jobs': [
            {'employer':'NYPD',
             'position':'Officer',
             'start':'1990'},
            {'employer':'M.I.B.',
             'position':'Agent',
             'start':'1997'}
        ]
    }
]

@app.route("/")
def index():
    return( "Hello World! This is Flask." )
    
@app.route("/profiles", methods=['GET'])
def profiles():
    return( jsonify({'profiles':users}) )
    
@app.route("/profile/<string:id>", methods=['GET'])
def get_profile(id):
    user = [user for user in users if user['id'] == id]
    if len(user) == 0:
        abort(404)
    return( jsonify({'profile':user[0]}) )
    
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
