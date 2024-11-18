def secound_largest(arr):
    sorted_arr = sorted(arr, reverse = True)
    return sorted_arr[1]
        
def difference(arr):
    return max(arr)-min(arr)

def median(arr):
    sorted_arr = sorted(arr)
    n = len(arr)
    if n % 2 == 0:
        return sorted_arr[n//2]
    else:
        mid1 = sorted_arr[n//2-1]
        mid2 = sorted_arr[n//2]
        return (mid1+mid2)/2

def small_larg(arr):
    return min(arr),max(arr)

def string(arr):
    return '-'.join(map(str,arr))