# this print new line after every print statement
print("hello")
print("how")
print("are")
print("you")

print("hello", end="\n")
print("how", end="\n")
print("are", end="\n")
print("you", end="\n")

# this doesn't print new line by default end = "\n" so we add null value in the end attribute
print("hello", end=" ")
print("how", end=" ")
print("are", end=" ")
print("you", end=" ")


