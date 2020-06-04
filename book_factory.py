# We have a factory that builds 3 unique items (classes)
# These items should all inherit from a generic/"standard" parent class
# Methods to add, subtract, change the stock of an object (stock = number of items on hand)
# Include a price attribute for the Class #I made the price a class attribute instead of something that can be more customized.

#Does this make this class a global variable? I didn't put it into main() but it still works there. I think I should put it into main()?
class Book:
  stock = 100
  def __init__(self, book_title, author):
     self.book_title = book_title
     self.author = author

  def __str__(self):
      return "The book title is: {}, the author of this book is: {}, the current stock of the book is {} \
      the price of the book is {}".format(self.book_title, self.author, self.stock, self.price)

  def add_stock(self, num):
    self.stock += num


# book1 = Book("To Kill a Mockingbird", "Harper Lee") # uses the __init__ Function
# book1.add_stock(100)
# print(book1)

class Textbook(Book):
    price = 40
    stock = 100
    def __init__(self, subject, book_title, author):
        super().__init__(book_title, author) #This only works for Python3, Idk why my computer is still using python2 at times
        self.subject = subject

    def __str__(self):
        return "The book title is: {}, the author of this book is: {}, the current stock of the book is {} \
        the subject this book focuses on is: {}, the price of the book is {}".format(self.book_title, self.author, self.stock, self.subject, self.price)

    def add_stock(self, num):
        self.stock += num


class Fiction(Book):
    price = 10
    stock = 100
    def __init__(self, genre, book_title, author):
        super().__init__(book_title, author)
        self.genre = genre

    def __str__(self):
        return "The book title is: {}, the author of this book is: {}, the current stock of the book is {} \
        the genre of this book is: {}, the price of the book is {}".format(self.book_title, self.author, self.stock, self.genre, self.price)

    def add_stock(self, num):
        self.stock += num

class Nonfiction(Book):
    price = 25
    stock = 100
    def __init__(self, genre, book_title, author):
        super().__init__(book_title, author)
        self.genre = genre

    def __str__(self):
        return "The book title is: {}, the author of this book is: {}, the current stock of the book is {} \
        the genre of this book is: {}, the price of the book is {}".format(self.book_title, self.author, self.stock, self.genre, self.price)

    def add_stock(self, num):
        self.stock += num

def purchaseItems(item_name):
    cost = item_name.price * item_name.stock
    print("The total price of your order is " + str(cost))

#Other types of books, inherit from the generic Book class

# Write a Purchase function, that takes the item name (class name), amount of items to purchase
# returns a list of objects that are of that class
# we want a way to also print out and calculate the total cost

# Nonfiction.price = 50 # changes all prices for all existing objects

# We can simulate creating objects, purchasing objects, etc.
def main():

    book1 = Fiction("Fantasy Literature", "Harry Potter", "J. K. Rowling")
    book1.add_stock(200)
    print(book1)
    purchaseItems(book1)

    book2 = Textbook("Mathematics", "Advanced Mathematics", "Richard G. Brown")
    book2.add_stock(25)
    print(book2)
    purchaseItems(book2)

    book3 = Nonfiction("Autobiography", "The Autobiography of Benjamin Franklin", "Benjamin Franklin")
    book3.add_stock(50)
    print(book3)
    purchaseItems(book3)

main()
