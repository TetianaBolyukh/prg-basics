# Create a function identity_matrix(n) that returns an identity matrix(2D array) of size n
def identity_matrix(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

def print_matrix(matrix):
    for row in  matrix:
        print(' '.join(map(str,row)))

for dimension in [3,5,8]:
    matrix = identity_matrix(dimension)
    print_matrix(matrix)
    print()