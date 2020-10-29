class Car:
    wheels = 4
    def __init__(self):
        self.milage = 10
        self.company = "BMW"
c1 = Car()
c2 = Car()
c1.milage = 15
c2.company = 18

print(c1.company)

print(c2.milage)

print(c1.wheels)

print(Car.wheels)

Car.wheels = 5
print(c2.wheels)




