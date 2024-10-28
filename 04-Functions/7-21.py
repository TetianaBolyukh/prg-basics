###
# Define the function f(number1,number2,number3), which returns 
# the difference between the largest and smallest numbers
#
def f(number1,number2,number3):
    largest = max(number1,number2,number3)
    smallest = min(number1,number2,number3)
    difference = largest - smallest
    return difference

print(f(7,4,9))
print(f(2,12,8))