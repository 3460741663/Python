import random

vocabulary = ['simple','hard','test','reliance','gleam','enforce','accuse',
              'sergeant','rating','hinge','cite','advocate','formidable',
              'gloom','shed','beyond','virtue','bizarre','draft','coupon',]

current_number = 1
while current_number <= 20: 
    print(vocabulary[random.randint(0,19)])
    current_number +=  1 


