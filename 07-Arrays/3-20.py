# Program to separate even and odd numbers of a given array of integers 
# Put all even numbers first, and then odd numbers
arr = [7,9,2,4,5,6]
new_arr = [num for num in arr if num % 2 == 0]+[num for num in arr if num % 2 != 0]
print(*new_arr)