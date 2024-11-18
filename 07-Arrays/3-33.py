#  Create a program that swaps the first and the last column
#  Print array values in rows and columns before and after changes
arr = [
    [1,3,5,7,9],
    [12,34,56,78,90],
    [2,4,6,8,0]
]
print('Values before changes:')
for row in arr:
    print(row)

for row in arr:
    row[0],row[-1] = row[-1],row[0]

print('')
print('Values after changes:')
for row in arr:
    print(row)