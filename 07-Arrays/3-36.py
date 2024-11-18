# Create a function that convert two-dimensional (2D) array into 1D
# Then create a program that prints 1D array for the following 2D arrays
def flatten_2d_array(array_2d):
    # Convert 2D array into 1D array
    result = []
    for row in array_2d:
        for element in row:
            result.append(element)
    return result

# List of 2D arrays
arrays = [
    [[2, 3], [1, 5]],
    [[5, 0, 3, 7, 5], [9, 0, 9, 1, 2]],
    [[2, 1], [3, 5], [7, 4], [2, 6]]
]

# Flatten each 2D array and print
for array_2d in arrays:
        print(flatten_2d_array(array_2d))