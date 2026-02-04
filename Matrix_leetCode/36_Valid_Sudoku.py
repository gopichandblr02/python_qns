"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
"""

"""
Why LeetCode still mentions O(1)
Even though we write loops, Big-O cares about growth.
| Problem type                | Complexity |
| --------------------------- | ---------- |
| n×n Sudoku                  | O(n²)      |
| **LeetCode 36 (fixed 9×9)** | **O(1)** ✅ |
"""

"""
Space complexity (bonus points)
We store:
9 row sets
9 column sets
9 box sets
Max elements = 9 × 9 = 81
Also constant → O(1) space.
"""

class Solution:
    def isValidSudoku(self, board) -> bool:
        seen = set()
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val != ".":
                    if (val, r) in seen or (c, val) in seen or (r // 3, c // 3, val) in seen:
                        return False
                    seen.add((val, r))
                    seen.add((c, val))
                    seen.add((r // 3, c // 3, val))
        return True


sol=Solution()
print(sol.isValidSudoku(board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))
# Output: True

print(sol.isValidSudoku(board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))
# Output: False