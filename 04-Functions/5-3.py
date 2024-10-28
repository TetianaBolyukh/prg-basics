###
# Allows to enter and print employee data. Due to personal
# data protection, you can determine whether information about
# the employee's salary will be printed
#
# your own defined module

# Reads employee's data from keyboard
from keyboard1 import input_string 
first_name = input_string('Enter name: ')
last_name = input_string('Enter surname: ')

from keyboard1 import input_integer
age = input_integer('Enter age: ')

from keyboard1 import input_real
salary = input_real('Enter salary: ')

from keyboard1 import input_boolean
is_salary_hidden = input_boolean('Hide salary? (y/n)')

# Prints employee's record
print('DATA RECORD')
print('===========')
print(f'Name: {first_name} {last_name}')
print(f'Age: {age}')
print(f'Salary: {salary}')
if is_salary_hidden == 'n':
    print('Salary')