distance = int(input('Enter distance: '))
hours = int(input('Enter hours: '))
minutes = int(input('Enter minutes: '))

avg_speed = lambda distance,hours,minutes: distance/(hours + minutes/60)

result = avg_speed(distance,hours,minutes)
print(f'Average speed: {result}')