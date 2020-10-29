#print value from dictionary by using index

my_dict = {'dave':'001','ava':'002','joe':'003' }
print(my_dict['dave'])

#print values only using value function

print(my_dict.values())

#print dictonary by using value

print(my_dict.get('ava'))
print(my_dict)

#using for loop in dictionary

for dictionary in my_dict:
    print(dictionary)


for x,y in my_dict.items():
    print(x,y)

#update dictionary
my_dict['dave'] = '004'
print(my_dict)


#Add element in dictionary
my_dict['chris'] = '005'
my_dict['dan'] = '007'
my_dict['cirus'] = '008'
print(my_dict)

#deleting elements

my_dict.pop('ava')
print(my_dict)

#deleting last item from dictionary

my_dict.popitem()
print(my_dict)

#deleting using del function

del my_dict['joe']
print(my_dict)

#converting dict in to panda dataframe

emp_details = {'employee' : {'dave' : {'id' : '001', 'salary' : '15000', 'designation' : 'team lead'},
                             'ava' : {'id' : '001', 'salary' : '20000', 'designation' : 'associate'}}}


import pandas
dataF = pandas.dataframe(emp_details['employee'])
print(dataF)















