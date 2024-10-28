###
# Converts a decimal number into a binary number
#

binary = decimal = int(input("Enter decimal number: "))

if decimal == 0:
    binary = 0
while decimal > 0:
    remainder = decimal % 2
    binary = str(remainder) + binary
    decimal = decimal // 2
print(f"{decimal}(10) = {binary}(2)")