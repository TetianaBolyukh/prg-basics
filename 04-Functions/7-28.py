###
# The sequence of digits contains the number of points rolled with a dice. 
# Define a function f(dice) that returns a number specifying the number of 
# dice rolled the most times in a row
#
def f(dice):
    max_digit = dice[0]
    max_count = 1
    current_count = 1
    for digit in range(1, len(dice)):
        if dice[digit] == dice[digit-1]:
            current_count += 1
        else:
            if current_count > max_count:
                max_digit = dice[digit - 1]
                max_count = current_count
            current_count = 1
    if current_count > max_count:
        max_digit = dice[-1]
        max_count = current_count
    return max_digit
print(f("5233165554211"))
print(f("2133"))