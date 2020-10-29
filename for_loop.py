fruits = ['apple','mango','grapes','kiwi']

''' for fruit_list in fruits:
    print(fruit_list) '''

num = int(input('number :'))
factorial = 1
if num < 0:
    print("number must be positive !")
elif num == 0:
    print('factorial = 1')
else:
    for i in range(1,num + 1):
        factorial = factorial*i
print(factorial)
