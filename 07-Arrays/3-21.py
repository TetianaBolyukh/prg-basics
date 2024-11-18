# Checks whether the first array is a subset of the second one 
# (whether all elements of the first array appear in the second array)
arr1 = [7,9,2,4,5,6]
arr2 = [2,4,6,7,9,5]
def check(arr1,arr2):
    for i in arr1:
        if i not in arr2:
            return False
    return True
print(check(arr1,arr2))