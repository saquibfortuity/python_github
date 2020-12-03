class person:
    country = "india"
    def __init__(self):
        print("initializing person class..\n")


    def takebreath(self):
        print("i m breathing... ")

class Employee(person):
    company = "honda "
    def __init__(self):
        print("initializing employee class")

    def getsalary(self):
        print(f"salary is {self.salary}")

    def takebreath(self):
        super().takebreath()
        print(" i am employee ")

class programmer(Employee):
    company = "fibverr"

    def getsalary(self):
        print(f"no salary for programmer")

    def takebreath(self):
        super().takebreath()
        print(" i am programmer so i am breathing++ ")

p = person()
p.takebreath()

e = Employee()
e.takebreath()

pr = programmer()
pr.takebreath()
