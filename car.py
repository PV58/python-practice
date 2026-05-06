from IPython.core import formatters
from IPython.core import formatters
class Car: ##def is used for defining function and init stands for initializing and 2 underscroll is necessary
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

## method

    def drive(self):
        print(f"The {self.model}{self.year} {self.color} is driving!") 
        ## self is refering to the object of the class which is car1, car2 and car3

    def stop(self):
        print(f"The {self.model} {self.year} {self.color} has stopped.")

    def describe(self):
        print(f"The {self.model} {self.year} {self.color} is for sale!") 

