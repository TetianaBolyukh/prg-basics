# Calculates and prints the number of even values in the array. Use the ‘while’ loop statement
arr = [34,7,19,4,21,8]
even = 0
i = 0
while i < len(arr):
    if arr[i] % 2 == 0:
        even += i
    i += 1
print(even)