arr = [2,3,2,5,8,1,9,8]
unique_elements = [num for num in arr if arr.count(num) == 1]
print(*unique_elements)