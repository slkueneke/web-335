"""
Title: TheHive-Assignment9.2
    Author: Shannon Kueneke and Kaitlyn Kelly
    Date: 3/11/26
    Description: What A Book Delivery
"""


#connect to mongodb database
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client['test']

# display a list of books
# formatted so it's easy to read
print("\n")
print("Books:")

# find every document in books collection
allBooks = db.books.find()

# loop through each book and print results
for document in allBooks:
    print(f"{document['title']} by {document['author']} in the {document['genre']} genre")

print("\n")

# prompt user to select a genre
genreChoice = input("Choose a genre: \n1) Classics \n2) Thrillers \n3) Horror \n\nYour choice: \n")

# store genre title in variable based on selection
# error handling for invalid selection, repeat prompt
if genreChoice == "1":
    genre = "classics"
elif genreChoice == "2":
    genre = "thriller"
elif genreChoice == "3":
    genre = "horror"
else:
    print("Invalid selection. Enter the number that corresponds to your genre choice.")
    print("\n")
    genreChoice = input("Choose a genre: \n1) Classics \n2) Thrillers \n3) Horror \nYour choice: \n")

# find every document in the books collection that matches the selected genre
allGenres = db.books.find({"genre": genre})

print("\n")
print("Books in " + genre.capitalize() +":")

# loop through the matching books and print the results
for books in allGenres:
    print(f"{books['title']} by {books['author']}")

print("\n")

# prompt user to enter a customer Id
customerId = input("Enter a Customer ID to view their wishlist: \n")

# find matching customer
customer = db.customers.find_one({"customerId": customerId})

# if valid customer, print their wishlist by title
if customer:

   # store customer's wishlist array
   wishlist = customer["wishlistitems"]

   print(f"\nWishlist items for customer {customerId}:")

   # for each bookId in their wishlist, find and print the corresponding title
   for bookId in wishlist:
      book = db.books.find_one({"bookId": bookId})
      print(book["title"])
      print("\n")

# if not a valid customer, print invalid message and exit program
if not customer:
   print("\nInvalid Customer Id.")
   exit()