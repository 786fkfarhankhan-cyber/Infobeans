# # 16. Train Reservation System
# # Problem

# # Design ticket reservation system.

# # Requirements

# # Train should contain:

# # train number
# # total seats
# # booked seats
# # Functionalities
# # Reserve seat
# # Cancel seat
# # Display available seats


# class Train:
#     def __init__(self, train_number, total_seats, booked_seats):
#         self.__train_number = train_number
#         self.__total_seats = total_seats
#         self.__booked_seats = booked_seats

#     def reserve_seat(self, seats):
#         if seats <= 0:
#             print("Invalid number of seats.")
#         elif self.__booked_seats + seats <= self.__total_seats:
#             self.__booked_seats += seats
#             print(seats, "seat(s) reserved successfully.")
#         else:
#             print("Sorry! Seats are not available.")

#     def cancel_seat(self, seats):
#         if seats <= 0:
#             print("Invalid number of seats.")
#         elif seats <= self.__booked_seats:
#             self.__booked_seats -= seats
#             print(seats, "seat(s) cancelled successfully.")
#         else:
#             print("Cancellation failed. Invalid number of booked seats.")

#     def display_available_seats(self):
#         available = self.__total_seats - self.__booked_seats
#         print("Train Number:", self.__train_number)
#         print("Total Seats:", self.__total_seats)
#         print("Booked Seats:", self.__booked_seats)
#         print("Available Seats:", available)



# t1 = Train("T101", 100, 80)

# print("----- Initial Train Details -----")
# t1.display_available_seats()

# print("\n----- Reserving Seats -----")
# t1.reserve_seat(10)

# print("\n----- After Reservation -----")
# t1.display_available_seats()

# print("\n----- Cancelling Seats -----")
# t1.cancel_seat(5)

# print("\n----- Final Train Details -----")
# t1.display_available_seats()

