###
# Products are marked with a special code consisting of 3 digits and a fourth 
# control digit. The forth digit is determined by calculating the remainder of 
# dividing the sum of the first three digits by 7. Define a function f(product_code) 
# that returns True if the product code is correct or False otherwise
#
def f(product_code):
    for digit in product_code:
        fourth_digit = (int(product_code[0]) + int(product_code[1]) + int(product_code[2])) % 7
        if int(product_code[3]) == fourth_digit:
            return True
        else:
            return False
    return True

print(f("1082"))
print(f("2035"))
print(f("1114"))
print(f("7071"))