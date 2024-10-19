###
# Calculates the parking fee based on the number of hours the car was parked 
#1-2 hours: 5 PLN
#3-6 hours: 15 PLN
#Over 6 hours: 20 PLN
hours = int(input('Enter the number of hours of parking: '))
if hours > 6:
    print(f'The fee is 20 PLN')
elif hours >= 3:
    print(f'The fee is 15 PLN')
elif hours >= 1:
    print(f'The fee is 5 PLN')
elif hours == 0:
    print('Parking is free')
elif hours < 0:
    print('Wrong number')