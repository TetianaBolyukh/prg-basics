# Calculates and prints the array and the arithmetic mean of array values. Use the “for” loop statement
arr = [15, 8, 31, 47, 2, 19]
sum = 0
count = 0
for i in arr:
    sum += i
    count += 1
    i += 1
result = sum / count
print('Array:', *arr)
print('Arithmetic mean:', result)
