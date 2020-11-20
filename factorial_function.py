n = int(input("enter number for factorial "))

def factorial(n):
    product = 1
    for i in range(n):
        product = product * (i+1)
    return product

print(factorial(n))

def factorial_recurrsive(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial_recurrsive(n-1)

print(factorial_recurrsive(n))







