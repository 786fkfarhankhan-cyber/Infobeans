# Book Library
# Create a class Book with fields: title, author, and price.
# Use setters to assign values and a method to print book details.

class Book:
    def __init__(self,title,author,price):
        self.__title = title
        self.__author = author
        self.__price = price
    def book_details(self):
        print(f"Title : {self.__title} \nAuthor Name : {self.__author} \nPrice : {self.__price}")

book_1 = Book("The Kingdom Of Haven","Louis",1000)
book_2 = Book("The Knights","William",600)
book_3 = Book("The 7 Good Habits","Captain",760)

book_1.book_details()
print()
book_2.book_details()
print()
book_3.book_details()












