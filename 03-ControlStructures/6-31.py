###
# Prints 20 integer random numbers in the range of 5 to 10
#
count = 0
import random

while count <= 20:
    print(random.randint(5,10), end = ' ')
    count += 1