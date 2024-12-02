
def binary_convert(number):
    stack = []

    while number > 0:
        remainder = number%2
        stack.append(remainder)
        number = number//2
        binary_number = ''
    while stack:
        binary_number += str(stack.pop())
    return binary_number

number = 18
print('Natural number:',number)
print('Binary number:',binary_convert(number))