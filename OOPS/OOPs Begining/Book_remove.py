# 5. Write a Python program to create a class called "Book" with attributes for title, author, and ISBN, and methods to add and remove books from a collection.


class Book:
    def __init__(self, title, author, isbn):
        self.__title = title
        self.__author = author
        self.__isbn = isbn

    def add_book(self, book):
        book.append(self)

    def remove_book(self, book):
        if self in book:
            book.remove(self)
            print("Book Removed Successfully")
        else:
            print("Book Not Found")

    def book_details(self):
        print(f"Title: {self.__title}")
        print(f"Author Name: {self.__author}")
        print(f"ISBN: {self.__isbn}")



book = []


book_1 = Book("The Kingdom Of Haven", "Louis", 1000)
book_2 = Book("The Knights", "William", 600)
book_3 = Book("The 7 Good Habits", "Captain", 760)


book_1.add_book(book)
book_2.add_book(book)
book_3.add_book(book)


print("Before Removing:")

for books in book:
    books.book_details()
    print()


book_1.remove_book(book)


print("After Removing:")

for books in book:
    books.book_details()
    print()












