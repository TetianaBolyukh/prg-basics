###
# Prints a lottery coupon (numbers from 1 to 49)
#
for i in range(7):
    for j in range(7):
        number = j * 7 + i + 1
        print(number, end = ' ')
    print()