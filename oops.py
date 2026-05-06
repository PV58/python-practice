class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale


car1 = Car("Tesla", 2022, "Red", True)

print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)



