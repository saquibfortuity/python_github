with open('sample2.txt','r')as f:
    a = f.read()
    print(a)
    f.close()


with open('sample2.txt','w')as f:
    a = f.write('sample2.txt for testing write function in python with write mode')
    print(a)
    f.close()

