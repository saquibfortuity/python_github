l1 = [5, 7, 9, 11]
l2 = [5, 10, 15, 20]
l3 = [5, 7, 9, 14]

if l2[0] - l2[1] == l2[1] - l2[2] and l2[1] - l2[2] == l2[2] - l2[3]:
    print("constant regression")
else:
    print("not constant")