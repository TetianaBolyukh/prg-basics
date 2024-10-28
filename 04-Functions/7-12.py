###
# Define a function f(n) that returns a string of n asterisks, separated by a slash sign
#
def f(n):
    result = ''
    for i in range(n):
        if i > 0:
            result += '/'
        result += '*'
    return result
print(f(4))
print(f(1))