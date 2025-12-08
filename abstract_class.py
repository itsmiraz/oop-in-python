
# Abstract Class : A class that cannnot be instantiated on its own; meant to be sublcassed.
#                  then can contain abstract  methods, which are declared but have no implementation.
#                   abstract classes benefits:
#                   1. prevents instantiation of the class itself
#                   2. requires children to use inherited abstract methods


from abc import ABC, abstractmethod


class Vehicle (ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def go(self):
        print('You drive the car')

    def stop(self):
        print('You stop the car')


class Motorcycle(Vehicle):

    def go(self):
        print('You ride the cycle')

    def stop(self):
        print('You stop the cycle')


class Boat(Vehicle):

    def go(self):
        print('You sail the cycle')

    def stop(self):
        print('You stop the cycle')


car = Car()
bike = Motorcycle()
boat = Boat()

car.go()
car.stop()


bike.go()
bike.stop()
