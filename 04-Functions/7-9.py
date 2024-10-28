###
# Create a function f(number, even) that computes the sum of the digits of a number. 
# When the value of the even parameter is True, the function returns the sum of 
# the even digits. When the value of the even parameter is False, the function 
# returns the sum of the odd digits
#
def f(number, even):
    result = 0
    if even == True:
        for i in str(number):
            i = int(i)
            if i % 2 == 0:
                result += i
    if even == False:
        for i in str(number):
            i = int(i)
            if i % 2 != 0:
                result += i
    return result
print(f(3124,True))
print(f(3124,False))
print(f(20576,False))
print(f(20576,True))
print(f(13115,True))