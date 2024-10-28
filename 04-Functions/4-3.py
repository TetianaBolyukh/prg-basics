###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#

a = int(input('Enter first side length: '))
b = int(input('Enter second side length: '))
c = int(input('Enter third side length: '))
import math
def triangle_area(a,b,c):
    s = (a+b+c)/2
    triangle_area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return triangle_area
result = triangle_area(a,b,c)
print(f'The area of a triangle with sides {a}, {b}, {c} is {result}')