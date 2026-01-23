# recursion_problems_solutions.py
# Python solutions for all 50 recursion problems from
# "Top 50 Interview Problems on Recursion & Algorithm" (GeeksforGeeks)
# https://www.geeksforgeeks.org/top-50-interview-problems-on-recursion-algorithm/?utm_source=chatgpt.com

# -------------------------------
# EASY RECURSION PROBLEMS
# -------------------------------

# 1. Print 1 to n without loops
def print_1_to_n(n):
    if n == 0:
        return
    print_1_to_n(n-1)
    print(n, end=' ')

# 2. Print n to 1 without loops
def print_n_to_1(n):
    if n == 0:
        return
    print(n, end=' ')
    print_n_to_1(n-1)

# 3. Mean of array
def mean_array(arr, n):
    if n == 0:
        return 0
    return (arr[n-1] + (n-1) * mean_array(arr, n-1)) / n

# 4. Sum of natural numbers
def sum_natural(n):
    if n == 0:
        return 0
    return n + sum_natural(n-1)

# 5. Decimal to binary
def decimal_to_binary(n):
    if n == 0:
        return ''
    return decimal_to_binary(n//2) + str(n%2)

# 6. Sum of array
def sum_array(arr, n):
    if n == 0:
        return 0
    return arr[n-1] + sum_array(arr, n-1)

# 7. Reverse a string
def reverse_string(s):
    if len(s) == 0:
        return s
    return reverse_string(s[1:]) + s[0]

# 8. Length of string
def length_string(s):
    if s == '':
        return 0
    return 1 + length_string(s[1:])

# 9. Sum of digits
def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)

# 10. Sum of array via tail recursion
def sum_array_tail(arr, n, acc=0):
    if n == 0:
        return acc
    return sum_array_tail(arr, n-1, acc + arr[n-1])

# 11. First n Fibonacci numbers
def fibonacci(n):
    if n == 0: return 0
    if n == 1: return 1
    return fibonacci(n-1) + fibonacci(n-2)

# 12. Factorial
def factorial(n):
    if n == 0: return 1
    return n * factorial(n-1)

# 13. Min & Max in array
def min_max_array(arr, n):
    if n == 1:
        return arr[0], arr[0]
    min_rest, max_rest = min_max_array(arr, n-1)
    return min(arr[n-1], min_rest), max(arr[n-1], max_rest)

# 14. Palindrome check
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

# 15. Count set bits in integer
def count_set_bits(n):
    if n == 0:
        return 0
    return (n & 1) + count_set_bits(n >> 1)

# 16. Fibonacci series in reverse
def fibonacci_reverse(n):
    if n <= 1:
        return [n]
    series = fibonacci_reverse(n-1)
    series.append(series[-1] + series[-2])
    return series

# -------------------------------
# MEDIUM RECURSION PROBLEMS
# -------------------------------

# 17. Remove all adjacent duplicates
def remove_adjacent_duplicates(s):
    if len(s) <= 1:
        return s
    if s[0] == s[1]:
        return remove_adjacent_duplicates(s[1:])
    return s[0] + remove_adjacent_duplicates(s[1:])

# 18. Sort the queue
def sort_queue(q):
    if not q:
        return []
    x = q.pop(0)
    sorted_q = sort_queue(q)
    return insert_sorted(sorted_q, x)

def insert_sorted(q, x):
    if not q or x < q[0]:
        return [x] + q
    return [q[0]] + insert_sorted(q[1:], x)

# 19. Reversing a queue
def reverse_queue(q):
    if not q:
        return []
    x = q.pop(0)
    rest = reverse_queue(q)
    rest.append(x)
    return rest

# 20. Binary to Gray code
def binary_to_gray(n):
    if n == 0:
        return 0
    b = n
    b >>= 1
    return n ^ binary_to_gray(b)

# 21. Product of two numbers
def product(x, y):
    if y == 0: return 0
    if y > 0: return x + product(x, y-1)
    return -product(x, -y)

# 22. Printing pyramid patterns
def pyramid_pattern(n, i=1):
    if i > n:
        return
    print(' '*(n-i) + '*'*(2*i-1))
    pyramid_pattern(n, i+1)

# 23. Longest palindromic substring (length)
def longest_palindrome(s):
    def helper(i,j):
        if i>j: return 0
        if i==j: return 1
        if s[i]==s[j]:
            l = j-i-1
            if helper(i+1,j-1)==l:
                return 2+l
        return max(helper(i+1,j), helper(i,j-1))
    return helper(0,len(s)-1)

# 24. Tower of Hanoi
def tower_of_hanoi(n, source, aux, target):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n-1, source, target, aux)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n-1, aux, source, target)

# 25. Calculate nCr
def nCr(n, r):
    if r == 0 or r == n:
        return 1
    return nCr(n-1, r-1) + nCr(n-1, r)

# 26. Geometric sum of series
def geometric_sum(k):
    if k == 0:
        return 1
    return 1/(2**k) + geometric_sum(k-1)

# 27. Convert string to integer
def str_to_int(s):
    if len(s) == 0:
        return 0
    return str_to_int(s[:-1])*10 + int(s[-1])

# 28. Subsets of a set
def subsets(s):
    if not s:
        return [[]]
    rest = subsets(s[1:])
    return rest + [[s[0]] + x for x in rest]

# 29. All paths from top-left to bottom-right
def all_paths(matrix, i=0, j=0, path=''):
    rows = len(matrix)
    cols = len(matrix[0])
    if i >= rows or j >= cols:
        return []
    if i == rows-1 and j == cols-1:
        return [path + matrix[i][j]]
    return all_paths(matrix,i+1,j,path+matrix[i][j]) + all_paths(matrix,i,j+1,path+matrix[i][j])

# 30. All combinations of balanced parentheses
def balanced_parentheses(n):
    def generate(s='', left=0, right=0):
        if len(s) == 2*n:
            result.append(s)
            return
        if left < n:
            generate(s+'(', left+1, right)
        if right < left:
            generate(s+')', left, right+1)
    result=[]
    generate()
    return result

# 31. Longest Common Subsequence (LCS)
def lcs(X, Y, m=None, n=None):
    if m is None: m=len(X)
    if n is None: n=len(Y)
    if m==0 or n==0:
        return 0
    if X[m-1]==Y[n-1]:
        return 1+lcs(X,Y,m-1,n-1)
    else:
        return max(lcs(X,Y,m-1,n), lcs(X,Y,m,n-1))

# -------------------------------
# HARD RECURSION PROBLEMS
# -------------------------------

# 32. Permutations of given string
def string_permutations(s):
    if len(s) <=1:
        return [s]
    perms=[]
    for i,c in enumerate(s):
        for p in string_permutations(s[:i]+s[i+1:]):
            perms.append(c+p)
    return perms

# 33. Josephus problem
def josephus(n,k):
    if n==1:
        return 0
    return (josephus(n-1,k)+k)%n

# 34. Number raised to its reverse
def power_reverse(n):
    rev=int(str(n)[::-1])
    return n**rev

# 35. Flood Fill algorithm
def flood_fill(mat,x,y,new_color,old_color=None):
    if old_color is None:
        old_color=mat[x][y]
    if x<0 or y<0 or x>=len(mat) or y>=len(mat[0]) or mat[x][y]!=old_color:
        return
    mat[x][y]=new_color
    flood_fill(mat,x+1,y,new_color,old_color)
    flood_fill(mat,x-1,y,new_color,old_color)
    flood_fill(mat,x,y+1,new_color,old_color)
    flood_fill(mat,x,y-1,new_color,old_color)

# 36. Sort a stack by recursion
def sort_stack(stack):
    if not stack:
        return []
    x=stack.pop()
    sorted_stack=sort_stack(stack)
    return insert_stack(sorted_stack,x)

def insert_stack(stack,x):
    if not stack or x>stack[-1]:
        stack.append(x)
        return stack
    val=stack.pop()
    stack=insert_stack(stack,x)
    stack.append(val)
    return stack

# 37. All palindromic partitions
def palindromic_partitions(s):
    def is_palindrome(s):
        return s==s[::-1]
    def dfs(path,remaining,res):
        if not remaining:
            res.append(path)
            return
        for i in range(1,len(remaining)+1):
            prefix=remaining[:i]
            if is_palindrome(prefix):
                dfs(path+[prefix],remaining[i:],res)
    res=[]
    dfs([],s,res)
    return res

# 38. Scrambled strings
def is_scramble(s1,s2):
    if s1==s2:
        return True
    if sorted(s1)!=sorted(s2):
        return False
    n=len(s1)
    for i in range(1,n):
        if (is_scramble(s1[:i],s2[:i]) and is_scramble(s1[i:],s2[i:])) or (is_scramble(s1[:i],s2[-i:]) and is_scramble(s1[i:],s2[:-i])):
            return True
    return False

# 39. Word Break problem
def word_break(s,wordDict):
    if s=='':
        return True
    for word in wordDict:
        if s.startswith(word):
            if word_break(s[len(word):],wordDict):
                return True
    return False

# 41. N-Queen problem
def solve_n_queen(n):
    def is_safe(board,row,col):
        for i in range(row):
            if board[i]==col or abs(board[i]-col)==row-i:
                return False
        return True
    def solve(board,row,res):
        if row==n:
            res.append(board[:])
            return
        for col in range(n):
            if is_safe(board,row,col):
                board[row]=col
                solve(board,row+1,res)
    res=[]
    solve([-1]*n,0,res)
    return res

# 42. Sudoku solver
def sudoku_solver(board):
    n=len(board)
    def is_valid(board,row,col,num):
        for i in range(n):
            if board[row][i]==num or board[i][col]==num:
                return False
        startRow=row-row%3
        startCol=col-col%3
        for i in range(3):
            for j in range(3):
                if board[startRow+i][startCol+j]==num:
                    return False
        return True
    def solve(board):
        for i in range(n):
            for j in range(n):
                if board[i][j]==0:
                    for num in range(1,10):
                        if is_valid(board,i,j,num):
                            board[i][j]=num
                            if solve(board):
                                return True
                            board[i][j]=0
                    return False
        return True
    solve(board)
    return board

# 43. Knight’s tour problem
def knight_tour(n):
    board=[[0]*n for _ in range(n)]
    moves=[(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]
    def is_safe(x,y,board):
        return 0<=x<n and 0<=y<n and board[x][y]==0
    def solve(x,y,movei):
        if movei==n*n:
            return True
        for dx,dy in moves:
            nx,ny=x+dx,y+dy
            if is_safe(nx,ny,board):
                board[nx][ny]=movei+1
                if solve(nx,ny,movei+1):
                    return True
                board[nx][ny]=0
        return False
    board[0][0]=1
    if solve(0,0,1):
        return board
    return None

# 44. N-digit numbers with difference K between adjacent digits
def numbers_with_diff(n,k):
    def dfs(num,remaining,res):
        if remaining==0:
            res.append(num)
            return
        last=num%10
        if last+k<=9:
            dfs(num*10+last+k,remaining-1,res)
        if k!=0 and last-k>=0:
            dfs(num*10+last-k,remaining-1,res)
    res=[]
    for i in range(1,10):
        dfs(i,n-1,res)
    return res

# -------------------------------
# END OF FILE
# -------------------------------
