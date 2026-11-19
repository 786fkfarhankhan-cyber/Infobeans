# 2. Vehicle System
# Create parent class Vehicle.
# Child classes:
# Car
# Bike
# Bus

# Add methods:

# start()
# stop()

from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass
class Car(Vehicle):
    def start(self):
        print("Car Start...")
    def stop(self):
        print("Car Stop...")

class Bike(Vehicle):
    def start(self):
        print("Bike Start...")
    def stop(self):
        print("Bike Stop...")

class Bus(Vehicle):
    def start(self):
        print("BUS Start...")
    def stop(self):
        print("BUS Stop...")

c = Car()
bu = Bus()
bi = Bike()

c.start()
c.stop()
bu.start()
bu.stop()
bi.start()
bi.stop()
