###
# Prints the first twenty words of the Fibonacci sequence
#
first_number = 0
second_number = 1
count = 20
print(first_number, second_number, end = ' ')
for i in range (count - 2):
    next_number = first_number + second_number
    print(next_number, end = '')
    first_number = second_number
    second_number = next_number