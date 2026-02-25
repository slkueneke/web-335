"""
Author: Shannon Kueneke
File: week-7/Kueneke_usersp2.py
Date: Feb 25, 2026
Description: Hands On 5.2: Python with MongoDB, Part II
"""

#import MongoClient
from pymongo import MongoClient
import datetime

#connect to db
uri = 'mongodb+srv://web335_user:s3cret@bellevueuniversity.llcll1z.mongodb.net/?appName=BellevueUniversity'
client = MongoClient(uri)

#config a variable to access web335DB
db = client['web335DB']

#reset the database so I can run this script many times without adding many Alexis Ffrenches
db.users.delete_many({"lastName": "Ffrench"})

#create a new user document - NOTE: my text editor said that datetime.datetime.utcnow() has been deprecated and to use the below method instead, so hopefully that's okay
ffrench = {
  "firstName": "Alexis",
  "lastName": "Ffrench",
  "employeeId": "1013",
  "email": "affrench@me.com",
  "dateCreated": datetime.datetime.now(datetime.timezone.utc)
}

#add new document to users collection
ffrench_user_id = db.users.insert_one(ffrench).inserted_id
print("****adding a new document*****")
print(ffrench_user_id)

#print new user document
print(db.users.find_one({"lastName": "Ffrench"}))
print("****end adding new document***")
print(" ")

#update email address of the document created above
print("****updating email address*****")

db.users.update_one(
  {"lastName": "Ffrench"}, 
  {
    "$set": {
      "email": "alexis@ffrench.com"
    }
  }
)

#print the document to show email is changed
print(db.users.find_one({"lastName": "Ffrench"}))
print("****end updating new email address*****")
print(" ")

#delete the above document
print("****deleting the new document*****")

db.users.delete_one({
  "lastName": "Ffrench"
})

#show the document has been completed
print(db.users.find_one({"lastName": "Ffrench"}))
print("****end deleting the new document*****")






