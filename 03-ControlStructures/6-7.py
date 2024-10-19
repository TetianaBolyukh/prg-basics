###
# Asks the user for their age and then checks which age group they belong to
# 
age = int(input('Enter your age to check the age group: '))
if age >= 65:
    print('Senior')
elif 20 <= age <= 64:
    print('Adult')
elif 13 <= age <= 19:
    print('Teen')
elif age < 0:
    print("Seems like you haven't been born yet")
elif age < 13:
    print('Child')
