setnumber = {10, 5, 65, 'saquib', 'python', 'flask', 10}
set2 = {'python', 'flask', 10}
print(set2)
print(setnumber)
# denoted by {}  does not show the duplicate value
# can store string and integer values
setnumber.add(2.6)
print(setnumber)
setnumber.copy()
print(setnumber)
set2 = setnumber.copy()
print(set2)
# copy makes the shallow copy of setnumber to set2

set2.difference()
print(setnumber.difference(set2))
A = {10, 20, 30, 40, 80}
B = {100, 30, 80, 40, 60, 80}
print (A.difference(B))
setnumber.difference_update()




