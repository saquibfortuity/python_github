class Employee:
    company = "camel"
    salary = 100
    location = "delhi"

  # def changesalary(self, sal):
  #    self.__class__.salary = sal

    @classmethod
    def changesalary(cls, sal):
        cls.salary = sal


emp = Employee
print(emp.salary)
emp.changesalary(50000)
print(emp.salary)
print(Employee.salary)

