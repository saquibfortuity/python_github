cources = {
           1: 'python',
           2: 'django',
           'third': "ml",
           3: "ml" # show this value bcoz the
           }
print(cources)

print(cources['third'])

cources[2] = 'flask'
print(cources)

cources['four'] = 'ml'
print(cources)

cources[5] = 'ai'
print(cources)
# """"print(cources(1))"""" can't call by index number
# denoted by {}  indexed changeable does not support duplicate values. unordered