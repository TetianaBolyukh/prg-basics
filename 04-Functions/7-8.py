###
# The vending machine accepts 1, 2 and 5 PLN coins. Define a function 
# f(amount_to_pay) that returns the minimum number of coins that can be 
# used to pay for the purchased product
#

def f(amount_to_pay):
    coins_5 = amount_to_pay//5
    remaining_coins_5 = amount_to_pay % 5
    coins_2 = remaining_coins_5//2
    remaining_coins_2 = remaining_coins_5 % 2
    coins_1 = remaining_coins_2
    sum = coins_5 + coins_2 + coins_1
    return sum
amount_to_pay = int(input("Enter the amount in PLN: "))
print(f'The minimum number of coins is: {f(amount_to_pay)}')