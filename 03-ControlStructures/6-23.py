###
# Creates a multiplication table in the range 1 to 10 for any number entered by the user
#
number = int(input("Enter number: "))
for i in range(1,11):
    multiplication_table = number * i
    print(f"{number}*{i}={multiplication_table}")