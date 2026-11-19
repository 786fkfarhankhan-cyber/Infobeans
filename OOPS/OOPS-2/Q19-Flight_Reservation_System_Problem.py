# 19. Flight Reservation System
# Problem

# Create airline reservation software.

# Requirements

# Flight should contain:

# flight number
# total seats
# booked seats
# Functionalities
# Book ticket
# Cancel ticket
# Prevent overbooking


class Flight:
    def __init__(self, flight_number, total_seats, booked_seats):
        self.__flight_number = flight_number
        self.__total_seats = total_seats
        self.__booked_seats = booked_seats

    def book_ticket(self, seats):
        if seats <= 0:
            print("Invalid number of seats.")

        elif self.__booked_seats + seats <= self.__total_seats:
            self.__booked_seats += seats
            print(f"{seats} Ticket(s) booked successfully.")

        else:
            print("Sorry! Not enough seats available.")

    def cancel_ticket(self, seats):
        if seats <= 0:
            print("Invalid number of seats.")

        elif seats <= self.__booked_seats:
            self.__booked_seats -= seats
            print(f"{seats} Ticket(s) cancelled successfully.")

        else:
            print("Cancellation failed. Invalid number of booked seats.")

    def available_seats(self):
        return self.__total_seats - self.__booked_seats

    def get_details(self):
        print(f"Flight Number: {self.__flight_number}")
        print(f"Total Seats: {self.__total_seats}")
        print(f"Booked Seats: {self.__booked_seats}")
        print(f"Available Seats: {self.available_seats()}")



f1 = Flight("AI101", 100, 80)

print("Initial Flight Details:")
f1.get_details()

print("\nBooking Tickets:")
f1.book_ticket(10)

print("\nAfter Booking:")
f1.get_details()

print("\nTrying to Overbook:")
f1.book_ticket(20)

print("\nCancelling Tickets:")
f1.cancel_ticket(5)

print("\nFinal Flight Details:")
f1.get_details()
















