class Calculator:
    def __init__(self, num):
        self.number = num

    def square(self):
        print(f"the square of {self.number} is {self.number **2}")

    def squareroot(self):
        print(f"the square root of {self.number} is {self.number **0.5}")

    def cube(self):
        print(f"the cube of {self.number} is {self.number **3} ")


num = int(input("enter the number for calculation :-  "))
# choice = input("for square press (1) for for squareroot press (2) for cuube press (3)")

ans = Calculator(num)
ans.square()
ans.squareroot()
ans.cube()

'''if 1:
    ans.square()

elif 2:
    ans.squareroot()

elif 3:
    ans.cube()'''


