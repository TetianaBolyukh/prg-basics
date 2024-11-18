arr = [7,3,8,5,2]
from MyArrays import secound_largest
from MyArrays import small_larg
from MyArrays import median
from MyArrays import string

print('Numbers:',','.join(map(str,arr)))
print('Second largest number:',secound_largest(arr))
print('Median:',median(arr))
print('Smallest and largest number:',small_larg(arr))
print('Numbers as a string:',string(arr))