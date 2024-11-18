import numpy as np

def transpose_matrix(m):
    return np.transpose(m)

def print_matrix(m):
    if isinstance(m[0], list):  
        for row in m:  
            print(' '.join(map(str, row)))
    else:
        for row in [m]: 
            print(' '.join(map(str, row)))

arr1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
arr2 = [
    [1,2,3,4,5],
    [6,7,8,9,0]
]
arr3 = [5,6,7,8]

print_matrix(arr1)
print()
print_matrix(arr2)
print()
print_matrix(arr3)