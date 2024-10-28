###
# Define the function f(n), which returns the n-th value of the Fibonacci sequence. 
# The sequence is defined as follows: the first value of the sequence is 0, the second 
# value is 1. Each subsequent value is the sum of the previous two
#
def f(n):
    first_number = 0
    second_number = 1
    for i in range(2, n):
        next_number = first_number + second_number
        first_number = second_number
        second_number = next_number
    return next_number
print(f(5))
print(f(9))