###
# Prints some array elements
#
arr = [2, 3, 7, 5, 4]

print(arr)
print('Number of elements', len(arr))
print('First value', arr[0])
print('Second value', arr[1])
print('Last value', arr[-1])
print('Last but one value', arr[len(arr)-1])
print('Sum of the first and last value', arr[0]+arr[-1])
print('Middle value', arr[len(arr)//2])
i = 0
while i < len(arr):
    print(arr[i], end=' ')
    i += 1