# Create a program that swaps the first and the last row
# Print array values in rows and columns before and after changes
arr = [
    [1,3,5,7,9],
    [12,34,56,78,90],
    [2,4,6,8,0]
]
print('Values before changes:')
for row in arr:
    print(' '.join(f'{i:2}' for i in row))

print('')

arr[0],arr[2] = arr[2],arr[0]
print('Values after changes:')
for row in arr:
    print(' '.join(f'{i:2}' for i in row))