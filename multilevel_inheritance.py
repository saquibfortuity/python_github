class person:
    country = "india"

    def takebreath(self):
        print("i m breathing... ")

class Employee(person):
    company = "honda "

    def getsalary(self):
        print(f"salary is {self.salary}")

    def takebreath(self):
        print("i am employee ")

class Programmer(Employee):
    company = "fibverr"

    def getsalary(self):
        print(f"no salary for programmer")

    def takebreath(self):
        print("i am programmer so i am breathing++ ")

p = person()
p.takebreath()

e = Employee()
e.takebreath()

pr = Programmer()
pr.takebreath()

# print(p.company)  --> this throws an error