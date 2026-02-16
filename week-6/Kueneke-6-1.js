/*
Shannon Kueneke
Feb 16, 2026
WEB 335
Hands On 6.1
*/

//display all students
db.students.find();

//add a new student and prove
newStudent = {
  firstName: "Bob",
  lastName: "Smith",
  studentId: "s1019",
  houseId: "h1009"
};
db.students.insertOne(newStudent);


//update one of that new student's properties and prove
db.students.updateOne({studentId:'s1019'}, {$set: {firstName: 'Robert'}});
db.students.findOne({studentId: 's1019'});

//delete the student and prove
db.students.deleteOne({lastName: 'Smith'});
db.students.findOne({lastName: 'Smith'});

//display all students by house: houses, students
db.houses.aggregate([ {$lookup: { from: 'students', localField: 'houseId', foreignField: 'houseId', as: 'students in house'}}]);

//display all students in house Gryffindor by Gryffindor, students 
db.houses.aggregate([ {$match: {'houseId': 'h1007'}}, {$lookup: { from: 'students', localField: 'houseId', foreignField: 'houseId', as: 'students in Gryffindor'}}]);


//display all students in the house with an Eagle mascot by house, students
db.houses.aggregate([
  {
    $match: { mascot: "Eagle" },
  },
  {
    $lookup: {
      from: "students",
      localField: "houseId",
      foreignField: "houseId",
      as: "students",
    },
  },
  {
    $project: {
      _id: 0,
      houseId: 1,
      students: {
        firstName: 1,
        lastName: 1,
        studentId: 1,
      },
    },
  },
]);

