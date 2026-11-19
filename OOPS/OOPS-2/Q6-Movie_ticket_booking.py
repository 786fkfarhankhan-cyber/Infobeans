class Movie:
    def __init__(self, movie_name, total_seats):
        self.__movie_name = movie_name
        self.__total_seats = total_seats
        self.__available_seats = total_seats
 
    def book_tickets(self, count):
        if count <= 0:
            print("Invalid ticket count")
        elif count <= self.__available_seats:
            self.__available_seats -= count
            print("Tickets booked")
        else:
            print("Not enough seats")
 
    def cancel_tickets(self, count):
        booked_seats = self.__total_seats - self.__available_seats
        if count <= 0:
            print("Invalid ticket count")
        elif count <= booked_seats:
            self.__available_seats += count
            print("Tickets cancelled")
        else:
            print("Invalid cancellation")
 
    def display_seats(self):
        print("Movie:", self.__movie_name)
        print("Available Seats:", self.__available_seats)
 
 
m1 = Movie("3 Idiots", 100)
m1.book_tickets(5)
m1.display_seats()
m1.cancel_tickets(2)
m1.display_seats()
