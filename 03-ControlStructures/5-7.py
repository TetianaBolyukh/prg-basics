import time

count_down = int(input('Enter the number of seconds to count down: '))

while count_down > 0:
    count_down -= 1
    if count_down == 5:
        print('five')
    if count_down == 4:
        print('four')
    if count_down == 3:
        print('three')
    if count_down == 2:
        print('two')
    if count_down == 1:
        print('one')
    time.sleep(1)
print("Time's up!")
