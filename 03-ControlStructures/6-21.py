###
# Program showing any amount (natural number) read from the keyboard with as few coins as possible
#
amount = int(input("Enter the amount in PLN: "))
coins_5 = amount//5
remaining_coins_5 = amount % 5
coins_2 = remaining_coins_5//2
remaining_coins_2 = remaining_coins_5 % 2
coins_1 = remaining_coins_2
print(f"""The amount of PLN {amount} in coins:
5 PLN coins: {coins_5}
2 PLN coins: {coins_2}
1 PLN coins: {coins_1}""")