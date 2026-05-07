## multiple inheritance  = inherit from more than on parent class 
##                          c(A, b)

# multi-level inheritance = inheritance from a parent class which inherits from another parent class 
                            # c(b) <- b(a) <- a()



class animal:


    def __init__(self,name):
        self.name=name

    def eat(self):
        print(f"this {self.name} can eat")
    def sleep(self):
        print(f"this {self.name} can sleep")

class prey(animal):
    def flee(self):
        print(f"this {self.name} can flee")

class predators(animal):
    def hunt(self):
        print(f"this {self.name} can  hunt")

class rabbit(prey):
    pass ##pass means do nothing/ skip

class hawk(predators):
    pass

class fish(predators, prey):
    pass

rabbit = rabbit("bugs") ## rabbit = rabbbit() means create object of rabbit class
hawk = hawk("tweety") ## it is necessary to pass the arguments 
fish = fish("nemo")

rabbit.eat()
hawk.hunt()
fish.flee()
fish.hunt()
fish.sleep()
fish.eat()
