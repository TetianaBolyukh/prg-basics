###
# In a separate module, define a function that checks if the number 
# is within the range <x, y>. The function returns a boolean value. 
# Then, create a program and use the function you defined. Sample result:
# A number: 7
# Number 7 in the range <2,15>: yes
from range import is_in_range
number = int(input('A number: '))
print(f'Number {number} in the range <2,15>: {is_in_range(number)}')