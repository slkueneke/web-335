/**
	  Title: books.js
    Author: Shannon Kueneke and Kaitlyn Kelly
    Date: March 4, 2026
    Description: MongoDB installation scripts for books and customers collections
 */

// Delete to reset the collections.
db.books.drop();
db.customers.drop();

// Create the collections using Document Validation.
db.createCollection("books", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      properties: {
        title: {
          bsonType: "string",
        },
        genre: {
          bsonType: "string",
        },
        author: {
          bsonType: "string",
        },
        bookId: {
          bsonType: "string"
        }
      },
    },
  },
});

db.createCollection("customers", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      properties: {
        firstName: {
          bsonType: "string",
        },
        lastName: {
          bsonType: "string",
        },
        customerId: {
          bsonType: "string",
        },
        wishlistitems: {
          bsonType: "array" //bookId in array
        }
      },
    },
  },
});

// Books
gatsby = {
  bookId: "001",
  title: "The Great Gatsby",
  author: "F. Scott Fitzgerald",
  genre: "classics"
};

emma = {
  bookId: "002",
  title: "Emma",
  author: "Jane Austen",
  genre: "classics"
};

shining = {
  bookId: "003",
  title: "The Shining",
  author: "Stephen King",
  genre: "horror"
};

girls = {
  bookId: "004",
  title: "Pretty Girls",
  author: "Karin Slaughter",
  genre: "thriller"
};

daughter = {
  bookId: "005",
  title: "The Good Daughter",
  author: "Karin Slaughter",
  genre: "thriller"
};

// Insert the books collection documents
db.books.insertOne(gatsby);
db.books.insertOne(emma);
db.books.insertOne(shining);
db.books.insertOne(girls);
db.books.insertOne(daughter);


// Customers

sam = {
  customerId: "1",
  firstName: "Sam",
  lastName: "Jones",
  "wishlistitems": ["001", "003"]
};

sonia = {
  customerId: "2",
  firstName: "Sonia",
  lastName: "Smith",
  wishlistitems: ["001", "004", "005"],
};

dan = {
  customerId: "3",
  firstName: "Dan",
  lastName: "Green",
  wishlistitems: ["005"],
};

megan = {
  customerId: "4",
  firstName: "Megan",
  lastName: "Baker",
  wishlistitems: ["002", "003", "005"],
};

chris = {
  customerId: "5",
  firstName: "Chris",
  lastName: "Flores",
  wishlistitems: ["002", "003"],
};


// Insert the documents.
db.customers.insertOne(sam);
db.customers.insertOne(sonia);
db.customers.insertOne(dan);
db.customers.insertOne(megan);
db.customers.insertOne(chris);

