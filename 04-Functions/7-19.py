###
# Define a function f(number) that returns the sum of repeated digits in a number
#
def f(number):
    count = {}
    for digit in str(number):
        if digit in count:
            count[digit] += 1
        else:
            count[digit] = 1
    sum = 0
    for digit in count:
        if count[digit] > 1:
            sum += int(digit) * count[digit]
    return sum
print(f(1027))
print(f(230335))
print(f(513553007))