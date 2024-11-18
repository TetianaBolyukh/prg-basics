# Define a function rand_elem(array) that returns a randomly selected array element.
# Using the function, print a few randomly selected array elements
import random
def rand_elem(array):
    return random.choice(array)
arr = [8,2,5,1,9]
print(rand_elem(arr))