# 19. Write a Python program to create a class with methods to search for flights and hotels, and to book and cancel reservations.



class ReservationSystem:
    def __init__(self):
        self.__flights = []
        self.__hotels = []
        self.__reservations = []

    def add_flight(self, flight_name, source, destination):
        flight = {
            "flight_name": flight_name,
            "source": source,
            "destination": destination
        }
        self.__flights.append(flight)

    def search_flights(self, source, destination):
        for flight in self.__flights:
            if flight["source"] == source and flight["destination"] == destination:
                print(flight)

    def add_hotel(self, hotel_name, city, price):
        hotel = {
            "hotel_name": hotel_name,
            "city": city,
            "price": price
        }
        self.__hotels.append(hotel)

    def search_hotels(self, city):
        for hotel in self.__hotels:
            if hotel["city"] == city:
                print(hotel)

    def book_reservation(self, reservation):
        self.__reservations.append(reservation)
        print("Reservation booked successfully")

    def cancel_reservation(self, booking_id):
        for reservation in self.__reservations:
            if reservation["booking_id"] == booking_id:
                self.__reservations.remove(reservation)
                print("Reservation cancelled")
                return

        print("Reservation not found")

r1 = ReservationSystem()

r1.add_flight("IndiGo", "Indore", "Delhi")
r1.add_flight("Air India", "Mumbai", "Delhi")

print("Available Flights:")
r1.search_flights("Indore", "Delhi")

r1.add_hotel("Taj Hotel", "Delhi", 5000)
r1.add_hotel("City Hotel", "Mumbai", 2500)

print("\nAvailable Hotels:")
r1.search_hotels("Delhi")

booking = {
    "booking_id": 101,
    "type": "Flight",
    "name": "IndiGo"
}

r1.book_reservation(booking)
r1.cancel_reservation(101)













