from functools import reduce

def add(x,y):
    return x+y

numbers = [2,4,6,3,7,5]
result = reduce(add, filter(lambda x: x%2==0, numbers))
print(result)