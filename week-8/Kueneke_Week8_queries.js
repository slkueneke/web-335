//Write a query to display a list of books.
db.books.find();

//Write a query to display a list of books by genre.
db.books.aggregate([{ $group: { _id: "$genre", books: { $push: "$title" } } }]);

//Write a query to display a list of books by author.
db.books.aggregate([{ $group: { _id: "$author", books: { $push: "$title" } } }]);

//Write a query to display a book by bookId.
db.books.findOne({bookId: '001'})