###
# Define the function f(n), which returns numbers from 1 to n as a string
#
def f(n):
    count = ''
    number = 0
    for number in range(0,n):
        number += 1
        count += str(number)
    return count
print(f(11))
print(f(4))