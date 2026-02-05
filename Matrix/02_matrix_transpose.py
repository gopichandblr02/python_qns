matrix = [[1, 2], [3, 4], [5, 6]]

# Transpose the matrix in different ways
# Method 1: Using nested loops
transposed1 = []
for i in range(len(matrix[0])):
    new_row = []
    for j in range(len(matrix)):
        new_row.append(matrix[j][i])
    transposed1.append(new_row)
print("Transposed using nested loops:")
print(transposed1)

# Method 2: Using list comprehension
transposed2 = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
print("Transposed using list comprehension:")
print(transposed2)
# Method 3: Using zip and unpacking
transposed3 = list(map(list, zip(*matrix)))
print("Transposed using zip and unpacking:")
print(transposed3)

# Method 4: Using numpy
import numpy as np
np_matrix = np.array(matrix)
transposed4 = np_matrix.T
print("Transposed using numpy:")
print(transposed4)


"""
✅ In-place transpose works ONLY for square matrices
Because swapping matrix[i][j] with matrix[j][i] assumes:
Row count == Column count
"""
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
# Method 5: Using In-place
n = len(matrix)
for i in range(n):
    for j in range(i + 1, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
print("Transposed in place:")
print(matrix)