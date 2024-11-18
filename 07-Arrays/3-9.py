# Compare(array1, array2) that returns True if both arrays are the same 
# or False otherwise. Two arrays are the same if they have the same number 
# of elements and values of elements in cells of arrays with the same index are equal 
# 1. ["water","book","sky"]   ["water","book","sky"]
# 1. [True,False]   [True,False,True]
# 1. [5,3,1]   [5,3,1]
# 1. [3,2,1]   [3,2]

def compare(arr1,arr2):
    if len(arr1) != len(arr2):
        return False
    for i in range(len(arr1)):
        if arr1[i] == arr2[i]:
            return True
        else:
            return False

arr1 = ["water","book","sky"]
arr2 = ["water","book","sky"]      
arr3 = [True,False]
arr4 = [True,False,True]
arr5 = [5,3,1]
arr6 = [5,3,1]
arr7 = [3,2,1]
arr8 = [3,2]

print(compare(arr1,arr2))
print(compare(arr3,arr4))
print(compare(arr5,arr6))
print(compare(arr7,arr8))