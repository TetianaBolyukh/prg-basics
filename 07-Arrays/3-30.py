# Create a program that modifies the array values to create a multiplication table
arr = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
    ] 
for i in range(5):
    for j in range(5):
        arr[i][j] = (i+1)*(j+1)
for row in arr:
    print(' '.join(f'{num:2}' for num in row))