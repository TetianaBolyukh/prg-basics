# Finds the smallest and largest values in the array and in which row and column they are located
arr = [[-38, 19], [5,40],[-7,11],[29,16]]
smallest = 0
largest = 0
s_position = (0,0)
l_position = (0,0)
for row in range(len(arr)):
    for i in range(len(arr[row])):
        value = arr[row][i]

        if value < smallest:
            smallest = value
            s_row = row
            s_column = i
        if value > largest:
            largest = value
            l_row = row
            l_column = i
print(f'The smallest value is {smallest}. It is located in {s_row} row, column {s_column}')
print(f'The largest value is {largest}. It is located in {l_row} row, column {l_column}')