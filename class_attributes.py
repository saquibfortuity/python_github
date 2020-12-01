class Employee:
    company = "Google"
    salary = 100

saquib = Employee()
md = Employee()
saquib.salary = 5000
md.salary = 6000

print(saquib.company)
print(md.company)
print(saquib.salary)
print(md.salary)
saquib.company = "Fortuitycorps"
print(saquib.company)
