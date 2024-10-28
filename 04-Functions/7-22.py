###
# A text contains any number of words. Define a function f(name) that returns the acronym
#
def f(name):
    result = ''
    words = name.split()
    for word in words:
        result += word[0]
    return result
print(f("Internet of Things"))