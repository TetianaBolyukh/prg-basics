###
# A palindrome is an expression that sounds the same when read backwards. 
# Define a function f(palindrome) that returns True if the expression is 
# a palindrome or False otherwise
#
def f(palindrome):
    if palindrome == palindrome[::-1]:
        result = True
    else:
        result = False
    return result
print(f("radar"))
print(f("12-11-21"))
print(f("book"))