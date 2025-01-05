number = int(input('Enter number: '))

is_even = lambda number: number%2

if is_even != 0:
    print(f'Number {number} is even')
if is_even == 0:
    print(f'Number {number} is odd')
