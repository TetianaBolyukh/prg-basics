###
# An expression contains operators for adding and subtracting single-digit numbers. 
# Define a function f(expression) that returns the value of the expression
#
def f(expression):
    current_operation = '+'
    result = 0
    for char in expression:
        if char.isdigit():
            number = int(char)
            if current_operation == '+':
                result += number
            if current_operation == '-':
                result -= number
        elif char in '+-':
            current_operation = char
    return result   
print(f("2+3"))
print(f("3+8+1"))
print(f("2+3-4+5-0"))