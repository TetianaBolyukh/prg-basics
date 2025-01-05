arr = list(range(1,20))
def power(x):
    powered = lambda x: x * x*x
    return powered(x)
powered = list(map(power, arr))
print(powered)