
# Creating a class named 'library' to store the books name and display this names and number of books present 
class library:

    # Constructor: called automatically when an object is created
    def __init__(self):
        # Variable to store the total number of books
        self.noBooks = 0

        # Empty list to store book names
        self.books = []

    # Method to add a new book to the library
    def addBook(self, book):

        # Add the given book name to the books list
        self.books.append(book)

        # Update the total number of books
        self.noBooks = len(self.books)

    # Method to display library information
    def showInfo(self):

        # Print the total number of books
        print(f"The library has {self.noBooks} books. The books are")

        # Loop through each book in the list and print it
        for book in self.books:
            print(book)

# Create an object of the library class
l1 = library()

# Add books to the library
l1.addBook("Harry potter1")
l1.addBook("Harry potter2")
l1.addBook("Harry potter3")

# Display the library information
l1.showInfo()
