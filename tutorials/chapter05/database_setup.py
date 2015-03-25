from pymongo import MongoClient

# (USE YOUR CONNECTION DETAILS FROM MONGOLAB)
MONGO_URL = 'mongodb://<uname>:<pass>@<database URL>'

# connect to the mongoDB server
client = MongoClient(MONGO_URL) 

# connect to the default database 
db = client.get_default_database()

# Here are two inital profiles for our database.
# Note that this looks just like JSON except that we need
# double-quotes ("") around the field names.
john =  { "_id" : 123,
          "fname" : "John",
          "lname" : "McClane",
          "jobs" : [ 
                    {"employer":"NYPD",
                     "position":"Lieutenant",
                     "start":1988}
                   ]
        }
j =     { "_id" : 456,
          "fname" : "James",
          "lname" : "Edwards",
          "jobs" : [
                    {"employer":"NYPD",
                     "position":"Officer",
                     "start":1990},
                    {"employer":"M.I.B.",
                     "position":"Agent",
                     "start":1997}
                   ]
        }
sam  =  { "_id" : 101,
          "fname" : "Samwise",
          "lname" : "Gamgee",
          "jobs" : [
                    {"employer":"Bag End",
                     "position":"Gardener",
                     "start":1954},
                    {"employer":"City of Hobbiton",
                     "position":"Mayor",
                     "start":1955}
                   ]
        }
        
# and now we use our database connection to store them
# in a new collection (think table), we'll call "profiles"
db.profiles.insert(john)
db.profiles.insert(j)
db.profiles.insert(sam)

