price = 88
#To control such values, add placeholders (curly brackets {}) in the text, and run the values through the format() method
txt = "The price is {} dollars"
print(txt.format(price))

# If you want to use more values, just add more values to the format() method:
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

name = "John"
age = 36
txt = "His name is {1}. {1} is {0} years old."
# Also, if you want to refer to the same value more than once, use the index number:
print(txt.format(age, name))
# for 0=age for 1=name
