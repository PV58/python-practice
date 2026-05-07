## abstract class = a class that cannot be instaniated on its own; meant to be subclassed. 
## they contain abstract methods which are methods that are declared but not implemented
## abstract classes benefits = prevents instantiation of the class itself. requires children to use inherited abstract methods

from abc import ABC, abstractmethod

class vehicle(ABC):
    @abstractmethod
    def go(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass

class car(vehicle):
    def go(self):
        print("The car is moving")
    def stop(self):
        print("The car is stopping")

class motorcycle(vehicle):
    def go(self):
        print("The motorcycle is moving")
    def stop(self):
        print("The motorcycle is stopping")

class boat(vehicle):
    def go(self):
        print("The boat is moving")
    def stop(self):
        print("The boat is stopping")

car = car()   
car.go()
car.stop() 

motorcycle = motorcycle()
motorcycle.go()
motorcycle.stop()  

boat = boat()
boat.go()
boat.stop()  

