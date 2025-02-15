"""
Below is the FizzBuzz Program from the earlier lesson. 
The rules for the program are: 

For the numbers from 1 to 30:

* If the number is evenly divisible by 5, print '🦡 badger'
* If the number is evenly divisible by 3, print '🍄 mushroom'
* If the number is evenly divisible by 15, print '🐍 snake!'
* If it is divisible by neither, print the number.

Your job is to modify only one line -- the one with range() 
-- so that the program only prints '🦡 badger'

Your program should print 4 badgers. 

"""
for i in range(1, 30):
    if i % 15 == 0: 
        print('snake')
    elif i % 3 == 0:
        print('badger')
    elif i % 5 == 0:
        print ('mushroom')
    else:
        print(i)
    # if i is divisible by 5, print 'badger'
    # if i is divisible by 3, print 'mushroom'
    # if i is divisible by 15, print 'snake'
    # if i is NOT divisible by 3, 5, or 15, print i

