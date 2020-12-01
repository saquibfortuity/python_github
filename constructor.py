class Employee:
    company = "google"

    def __init__(self, name, salary, subunit ):
        self.name = name
        self.subunit = subunit
        self.salary = salary
        print("Emmploye is created")

    def GetDetails(self):
        print(f"the name of employee is : {self.name}")
        print(f"the salary of employee is : {self.salary}")
        print(f"the subunit of employee is : {self.subunit}")

    def getSalary(self):
        print(f"salary of this employee working in {self.company} and salary is {self.salary}")

    @staticmethod
    def greet():
        print("Hello Good Morning ! ")


# user_name = input("enter name : ")

saquib = Employee("saquib", 50000, 'youtube')
# saquib = Employee() --> this throw an error
saquib.GetDetails()

