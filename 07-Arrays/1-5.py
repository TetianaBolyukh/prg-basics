###
# An array contains values: 1, 2, 3, 4, 5. Write a program that modifies the array values. Print the array after each change.

# subtract one from the first element of the array
# increase the last array element by 4
# multiple the middle array element by 2
arr = [0,2,3,4,5]
print('Array:', arr)
arr[0] -= 1
print('Array:', arr)
arr[-1] += 4
print('Array:', arr)
middle = len(arr)//2
arr[middle] *= 2
print('Array:', arr)
