class Employee:
    company = "VISA"
    Ecode = 4425

class Freelancer:
    company = "Fiverr"
    level = 0

    def upgradeLevel(self):
        self.level = self.level + 1

class programmer(Employee, Freelancer):
    name = "Saquib"

obj_programmer = programmer()
obj_programmer.upgradeLevel()
print(obj_programmer.level)
