###
# Define a function power(x, n) that calculates xn. Apply recursion. Then, calculate 53
#
def power(x,n):
    result = x*x**(n-1)
    return result
print(power(5,3))