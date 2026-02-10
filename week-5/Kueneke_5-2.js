/*
Author: Shannon Kueneke
Assignment 5.2
Date: Feb 10, 2026
*/


//add a new user to user collection
ffrench = {firstName: 'Alexis', lastName: 'Ffrench', employeeId: '1013', email: 'alexis@ffrench.com', dateCreated: new Date()};
db.users.insertOne(ffrench);

//show new user was successfully added
db.users.findOne({ lastName: 'Ffrench' });

//update Mozart's email to mozart@me.com
db.users.updateOne({lastName: 'Mozart'}, {$set:{email: 'mozart@me.com'}});

//show Mozart email is successfully updated
db.users.findOne({ email: 'mozart@me.com' });


//display all users, but only show the first name, last name, and email address
db.users.find({}, { firstName: 1, lastName: 1, email: 1, _id: 0 });
