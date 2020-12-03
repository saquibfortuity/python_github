class Employeee:
    company = "Google"

    def showdetails(self):
        print("this is an employee")


class programmer(Employeee):
    language = "Python"

    def getlanguage(self):
        print(f"the language is {self.language}")

obj_emp = Employeee()
obj_pr = programmer()

print(obj_emp.company)
print(obj_pr.company)
print(obj_pr.showdetails())

