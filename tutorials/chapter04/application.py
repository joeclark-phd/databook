#!venv/bin/python
from flask import Flask, jsonify, abort, request

application = Flask(__name__)

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

@application.route("/")
def index():
    return( "Hello World! This is Flask." )
    
@application.route("/profiles", methods=['GET'])
def profiles():
    return( jsonify({'profiles':users}) )
    
@application.route("/profile/<string:id>", methods=['GET'])
def get_profile(id):
    user = [user for user in users if user['id'] == id]
    if len(user) == 0:
        abort(404)
    return( jsonify({'profile':user[0]}) )
    
@application.route("/profiles", methods=['POST'])
def post_profile():
    if not request.json:
        abort(400) # 400 error = bad request
    users.append(request.json)
    return( jsonify({'profile':request.json}), 201 )
        
@application.route("/profile/<string:id>", methods=['PUT'])
def update_profile(id):
    user = [user for user in users if user['id'] == id]
    if len(user) == 0:
        abort(404)
    if not request.json:
        abort(400)
    users.remove(user[0])
    users.append(request.json)
    return( jsonify({'profile':request.json}) )
    
@application.route("/profile/<string:id>", methods=['DELETE'])
def delete_profile(id):
    user = [user for user in users if user['id'] == id]
    if len(user) == 0:
        abort(404)
    users.remove(user[0])
    return( "Deleted profile " + id )
    
@application.route("/companies")
def companies():
    return( "List of companies" )
    
@application.route("/company/<string:id>/profiles")
def company_profiles(id):
    return( "List of users who worked for company " + id )
    
if __name__ == '__main__':
    application.run(debug=True)
