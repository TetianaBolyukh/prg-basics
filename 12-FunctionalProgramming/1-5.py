# Enter distance in km: 70
# Enter number of travel hours: 1
# Enter number of travel minutes: 23
# Average speed: 50.6 km/h 

distance = int(input('Enter distance: '))
hours = int(input('Enter hours: '))
minutes = int(input('Enter minutes: '))

def avg_speed(distance,hours,minutes):
    time_h = hours + minutes/60
    avg_speed = distance/time_h
    return avg_speed

result = avg_speed(distance,hours,minutes)
print(f'Average speed: {result}')