# a = ('val1', (1, 2 ), (2.5, 5.6, 8.2))
# print(a)
# print(type(a))
# print(a[1][1])

'''b = [['gmc', 'audi', 'bmw', 'ford'], ['saquib', 'ayush', 'dan', 'maniac'], [1, 2, 3, 4], [2.3, 4.6, 8.2, 3.4]]
print(b)
print(type(b))
print(b[0][-1:-3])'''

lst = [1, 1, 2, 3, 3]
a = tuple(lst)
print(a)

b = list(a)
print(len(b))

c = set(b)
print(len(c))

d = list(c)
print(len(d))

x = range(1, 11, 1)
for i in x:
    print(i)

e = list(x)
print(type(e))




