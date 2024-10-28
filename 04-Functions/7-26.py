###
# Define a function f(text) that returns the given text 
# with all characters separated by a dash sign
#
def f(text):
    result = '-'.join(text)
    return result
print(f("Univesity"))
print(f("UE"))
print(f("x"))
print(f(""))