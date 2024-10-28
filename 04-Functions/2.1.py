###
# Program for testing built-in functions
# letter read from the keyboard
# number representing the string "20303"
# binary string representing decimal number 304
# hexadecimal string representing decimal number 304
# integer representing the Unicode code of the € sign
# absolute value of -17
#
max_number = max(7,5,6,3,8,2)
print('Max number of 7,5,6,3,8,2 is', max_number)

min_number = min(4,7,2,3,9,8)
print('Min number of 4,7,2,3,9,8 is', min_number)

str_length = len("computer science")
print('The number of characters in "computer science" is', str_length)

letter = input('Enter your letter: ')
print('The letter you entered is', letter)

str_number = int("20303")
print('The number representing the string "20303" is', str_number)

dec_number = 304
bin_number = bin(dec_number)
print('Binary string representing decimal number 304 is', bin_number)

dec_number = 304
hex_number = hex(dec_number)
print('Hexadecimal string representing decimal number 304 is', hex_number)

sign = "€"
integer = ascii(sign)
print('Integer representing the Unicode code of the € sign is', integer)

number = -17
abs_value = abs(number)
print('Absolute value of -17 is', abs_value)