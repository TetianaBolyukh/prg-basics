# Calculates and prints the array and the arithmetic mean of array values. Use the “while” loop statement
arr = [15, 8, 31, 47, 2, 19]
i = 0
sum = 0
count = 0
while i < len(arr):
    sum += arr[i]
    count += 1
    i += 1
result = sum / count
print('Array:', *arr)
print('Arithmetic mean:', result)