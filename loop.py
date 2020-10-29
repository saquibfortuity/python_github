#while is generally used when we dont know how many itteration is required
import random
n = 20
to_be_guess = int(n * random.random()) + 1
guess = 0
while guess != to_be_guess:
      guess = int(input('enter number :'))
      if guess > 0:
          if guess > to_be_guess:
              print('mumber is too large ')
          elif guess < to_be_guess:
              print('number is too small ')
      else:
          print('sorry wrong input ')
          break
else:
    print('you made it')

#when we fetch the data and dont know the exact number of outpur







