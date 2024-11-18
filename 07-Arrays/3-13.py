
num = 23
arr = [15,38,7,23,14]


if num in arr:
    result = True
else:
    result = False

print('Number:',num)
print('Array:',*arr)

if result == True:
    print('Result: number 23 appears in the array')
else:
    print('Result: number 23 does not appear in the array')