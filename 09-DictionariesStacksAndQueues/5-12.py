# Define a function that takes a string as input and uses a stack to reverse it. 
# Then, write a program to reverse any text entered from the keyboard

import queue
def reverse_string(string):
    reversed_str = ''
    stack = []

    for i in string:
        stack.append(i)

    while stack:
        reversed_str += stack.pop()
    return reversed_str
print(reverse_string('function'))
