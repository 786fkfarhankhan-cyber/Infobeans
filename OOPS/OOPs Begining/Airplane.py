# 12. Write a Java program to create a class called "Airplane" with a flight number, destination, and departure time attributes, and methods to check flight status and delay.

class Airplane:
    def __init__(self,flight_no,destination,departure_time):
        self.__flight_no = flight_no
        self.__destination = destination
        self.__departure_time = departure_time

    def check_flight(self):
        print(f"Flight Number = {self.__flight_no}")
        print(f"Destination = {self.__destination}")
        # print(f"Flight Departure Timing = {self.__departure_time} Time")
        print(f"Flight Departure Timing = {self.__departure_time[0]}:{self.__departure_time[1]:02d} AM")

    def delay_flight(self, delay_hours, delay_minutes):
        print(f"For {self.__destination} Flight will be delay....")
        print(f"Delay Hours = {delay_hours} Hr")
        print(f"Delay Min = {delay_minutes} Min")

        actual_hour = self.__departure_time[0] + delay_hours
        actual_minute = self.__departure_time[1] + delay_minutes

        if actual_minute >= 60:
            actual_hour += 1
            actual_minute -= 60

        # self.__actual_time = (actual_hour, actual_minute)

        
        print(f"Actual Time = {actual_hour}:{actual_minute:02d} AM")


    def check_flight_after_delay(self):
        print(f"Flight Number = {self.__flight_no}")
        print(f"Destination = {self.__destination}")
        # print(f"Flight Departure Timing = {actual_hour}:{actual_minute:02d} AM")
        print(f"Flight Departure Timing = {self.__departure_time[0]}:{self.__departure_time[1]:02d} AM")
  

    

f1 = Airplane(101,"Delhi",(9,30))
print()
f1.check_flight()
print()
f1.delay_flight(1,10)
print()

# f1.check_flight_after_delay()
        
f1.check_flight()















