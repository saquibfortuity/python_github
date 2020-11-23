# use open function toread the content
# by default it open in read mode

f = open('sample.txt')
#data = f.read()
# data = f.read(6)  # it reads first 6 character of file
# print(data)
data1 = f.readline()
print(data1)
f.close()
