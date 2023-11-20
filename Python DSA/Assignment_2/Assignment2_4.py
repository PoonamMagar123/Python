
# 4. Define a class Book with instance object variables bookid, title and price. 
# Initialise them via__init__() method. Also define method to show book variables

class Book:
    def __init__(self, bookid, title, price):
        self.bookid = bookid
        self.title = title
        self.price = price
    
    def showBookDetails(self):
        print("Book ID:", self.bookid)
        print("Title:", self.title)
        print("Price:", self.price)

def main():
    # Creating an instance of the Book class
    book1 = Book(1, 'Python Programming', 29.99)
    
    # Calling the showBookDetails method to display book information
    book1.showBookDetails()

if __name__ == "__main__":
    main()

# The Book class has instance variables bookid, title, and price which
# are initialized through the __init__ method.
# The showBookDetails() method is defined to display the book variables.
# In the main() function, an instance of the Book class is created, and 
# the showBookDetails() method is called to display the book information.