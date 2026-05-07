# inheritence = allows a clas to inherit attributes and methods of other class
# helps with code resuability and extensibility of code 
# parent class = class that is inherited from
# child class = class that inherits from the parent class

class animal:
    def __init__(self,name):
        self.name=name
        self.is_alive=True

    def eat(self):
        print(f"{self.name} is eating!")

    def sleep(self):
        print(f"{self.name} is asleep!")

class dog(animal):
    def __init__(self,name):
        self.name=name
        self.is_alive=True

    def eat(self):
        print(f"{self.name} is eating!")

    def sleep(self):
        print(f"{self.name} is aslee!")

class cat(animal):
    def __init__(self,name):
        self.name=name
        self.is_alive=True

    def eat(self):
        print(f"{self.name} is eating!")

    def sleep(self):
        print(f"{self.name} is asleep!")

class mouse(animal):
    def __init__(self,name):
        self.name=name
        self.is_alive=True

    def eat(self):
        print(f"{self.name} is eating!")

    def sleep(self):
        print(f"{self.name} is asleep!")

dog = dog("scooby")
cat = cat("tom")
mouse = mouse("jerry")

print(dog.name)
print(dog.is_alive)
dog.eat()
mouse.sleep()

