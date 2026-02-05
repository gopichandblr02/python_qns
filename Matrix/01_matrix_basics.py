"""
1️⃣ What is a Matrix in Python?
In Python, a matrix is usually represented as a list of lists.
"""
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
"""
Each inner list = a row
All rows should have the same length (important!)
"""
# Dimensions
rows = len(matrix)
cols = len(matrix[0])
# So this matrix is 3 × 3.

"""
2️⃣ Accessing Elements
Access a single element
"""
matrix[1][2]   # row 1, column 2 → 6
# Access a row
matrix[0]      # [1, 2, 3]
# Access a column
col = [matrix[r][1] for r in range(rows)]
# [2, 5, 8]

"""
3️⃣ Traversing a Matrix
Row-wise traversal (most common)
"""
for r in range(rows):
    for c in range(cols):
        print(matrix[r][c], end=" ")
    print()
# Pythonic version
for row in matrix:
    for val in row:
        print(val, end=" ")
    print()

"""
4️⃣ Common Matrix Patterns (VERY IMPORTANT)
4.1 Row-wise operations
Example: sum of each row
"""
for row in matrix:
    print(sum(row))
"""
4.2 Column-wise operations
Example: sum of each column
"""
for c in range(cols):
    col_sum = 0
    for r in range(rows):
        col_sum += matrix[r][c]
    print(col_sum)
"""
5️⃣ Matrix Transpose
What is Transpose?
Convert rows → columns
"""

"""
Original        Transpose
1 2 3           1 4
4 5 6   →       2 5
                3 6

"""

# Method 1: Create a new matrix
transpose = []
for c in range(cols):
    new_row = []
    for r in range(rows):
        new_row.append(matrix[r][c])
    transpose.append(new_row)

# Pythonic
transpose = list(zip(*matrix))

# ⚠️ In-place Transpose (ONLY for square matrix)
# ❌ Fails for non-square matrices
n = len(matrix)
for i in range(n):
    for j in range(i + 1, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

# 🔟 Time & Space Complexity Cheat Sheet
"""
| Operation          | Time       | Space |
| ------------------ | ---------- | ----- |
| Traverse           | O(mn)      | O(1)  |
| Transpose          | O(mn)      | O(mn) |
| In-place transpose | O(n²)      | O(1)  |
| Rotate             | O(n²)      | O(1)  |
| Spiral             | O(mn)      | O(mn) |
| Binary search      | O(log(mn)) | O(1)  |

"""


"""
🔥 Interview Tips (Listen carefully)
Always ask: square or rectangular matrix?
In-place operations usually mean square matrix
Index mapping questions = binary search + math
Boundaries shrinking = spiral / layers
Marker technique = use first row/column
"""



