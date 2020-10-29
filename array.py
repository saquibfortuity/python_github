import array as arr

a = arr.array ('i',[2,5,8,4,5,1,2])
print(a)

#import array as arr
#to declare array use arrayname = arr.array

#array length
print(len(a))

#add elements in array
a.append(7)
print(a)

#extend elements in array

a.extend([4,5])
print(a)

#insert value in array

a.insert(3,5)
print(a)

#remove element from array

a.pop()
print(a)
#remove element from array using remove

a.remove(5)

#concatination of array only for same datatype
#where i is type code and it refers to integer type for float we can use f and for every data type using type code in python
a = arr.array ('i',[2,5,8,4,5,1,2])
b = arr.array ('i',[6,4,3,2,7,1,8])
print(a)
print(b)

d = a+b
print(d)

#slicing of array

print(a[0:3])

#reverse of array
'''print(a[::-1])'''

#looping in an array

# for loop with array

for z in a:
    print(z)

#array using while loop
print(a)

temp = 2
while temp < len(a):
    print(a[temp])
    temp+=1

















