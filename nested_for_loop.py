'''from math import sqrt
n = int(input('miximal number'))
for a in range(1,n+1):
    for b in range(a,n):
        c_square = a**2 + b**2
        c = int(sqrt(c_square))
        if ((c_square - c**2)) == 0:
            print(a, b, c)'''
#ex of nested for
#program for printing pythogorean number

travelling = input('yes, no')
while travelling == ('yes'):
    num = int(input('enter the number of people travelling:'))
    for num in range(1, num + 1):
        name = input('name:')
        age = input('age:')
        gender = input('male or female:')
        print(name)
        print(age)
        print(gender)
    travelling = input('forgot someone!!!')
