###
# Calculates the sum of the digits in a number
#
def sum_digits(any_number):
    num = str(abs(any_number))
    sum = 0
    i = 0
    while i < len(num):
        sum += int(num[i])
        i += 1
    return sum

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')