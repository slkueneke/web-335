'''
Title: Kueneke_usersp1.py
Author: Shannon Kueneke
WEB 335 Week 6
Description: Hands On 4.2
Date: Feb 16, 2026
'''

#import MongoClient
from pymongo import MongoClient

#connect to db
uri = 'mongodb+srv://web335_user:s3cret@bellevueuniversity.llcll1z.mongodb.net/?appName=BellevueUniversity'
client = MongoClient(uri)

#config a variable to access web335DB
db = client['web335DB']


#display all documents in the users collection
print('***printing all docs in collection users***');
for user in db.users.find({}, {'firstName': 1}):
  print(user)

  
#display a document where the employeeId is 1011
print('***printing the user with employeeId 1011***');
print(db.users.find_one({'employeeId': '1011'}));

#display a document where the lastName is Mozart
print('***printing the user with lastName Mozart***');
print(db.users.find_one({'lastName': 'Mozart'}));

