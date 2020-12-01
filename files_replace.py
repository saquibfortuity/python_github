with open("replace.txt") as f:
    content = f.read()

content = content.replace("bitch", "%@##@%")

with open("replace.txt", 'w')as f:
    f.write(content)
print("unwanted words replaced ")


