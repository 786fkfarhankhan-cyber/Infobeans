
class Book:

    total_books = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

        Book.total_books += 1

    
    def issue_book(self):
        if self.available:
            self.available = False
            print("Book Issued")
        else:
            print("Already Issued")

    def return_book(self):
        if self.available == False:
            self.available = True
            print("Book Returned")
        else:
            print("Book Not Issued")

   
    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Available:", self.available)

    @classmethod
    def get_total_books(cls):
        return cls.total_books


b1 = Book("Python", "Guido")

b1.display()

b1.issue_book()
b1.issue_book()

b1.return_book()

b1.display()

print("Total Books:", Book.get_total_books())
