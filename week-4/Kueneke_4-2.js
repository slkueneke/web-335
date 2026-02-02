//display all users
db.users.find()

//display user with email jbach@me.com
db.users.findOne({email: "jbach@me.com"})

//display user with the last name Mozart
db.users.findOne({lastName: "Mozart"})

//display the user with the first name Richard
db.users.findOne({firstName: "Richard"})

//display the user with employeeId 1010
db.users.findOne({employeeId: "1010"})
