# For the given array of real numbers, prints the number of elements 
# that are greater than the given value entered from the keyboard
arr = [1,2,5,8,12,32,44,65,100]
string = ''
num = int(input('Enter you number: '))
for i in arr:
    if i > num:
        string += str(i) + ' '
print(string)