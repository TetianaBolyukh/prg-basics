###
# Write a program that prints numbers from 1 to 30.
# If the number is divisible by 3 then the program prints the word 'THREE'.
# Next, if the number is divisible by 5 then the program prints the word 'FIVE.
# Finally, if the number is divisible by both and 5 then the program prints the word 'BINGG
#
for i in range(1,31):
    if i % 3 == 0:
        print("THREE")
    if i % 5 == 0:
        print("FIVE")
    if i % 3 == 0 and 1 % 5 == 0:
        print("BINGO")
    print(i)