# **Recursion vs Iteration**
## **1. Definition**
### **Recursion**

# A function calling **itself** to solve smaller subproblems until a base condition is met.

### **Iteration**

# Using **loops** (`for`, `while`) to repeat operations until a condition is satisfied.

# **2. Key Differences**
"""
| Feature               | Recursion                                           | Iteration                                     |
| --------------------- | --------------------------------------------------- | --------------------------------------------- |
| **Approach**          | Divide problem into smaller subproblems; self-calls | Repeat a block of code until condition is met |
| **Control Structure** | Function calls                                      | Loops (`for`, `while`)                        |
| **Memory Usage**      | High (each call uses stack space)                   | Low (only loop variables)                     |
| **Termination**       | Base case                                           | Loop condition                                |
| **Performance**       | Slower due to call overhead                         | Faster                                        |
| **Readable for**      | Tree/graph problems                                 | Simple repetitive tasks                       |
| **Risk**              | Stack overflow                                      | Infinite loop                                 |
"""


# **3. Simple Examples**
## **Recursion Example: Factorial**
# ```python
def factorial(n):
    if n == 0:      # base case
        return 1
    return n * factorial(n - 1)

## **Iteration Example: Factorial**

def factorial_iter(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# **4. When to Use Which?**

### **Use Recursion When:**

# * Problem has a natural recursive structure
#   ✔️ Trees
#   ✔️ Graphs
#   ✔️ Divide & Conquer
#   ✔️ DFS / Backtracking

### **Use Iteration When:**

# * Repetitive tasks
# * Performance matters
# * Sequence-based problems
# * Avoiding stack overflow

# **5. Real Examples**

### **Recursion: DFS on a tree**

def dfs(node):
    if not node:
        return
    print(node.val)
    dfs(node.left)
    dfs(node.right)

### **Iteration: Loop through array**

for num in arr:
    print(num)

# **6. Pros & Cons**

## **Recursion**

# ✔️ Cleaner, elegant code
# ✔️ Good for hierarchical data
# ✖️ More memory usage
# ✖️ Can cause stack overflow

## **Iteration**

# ✔️ Efficient
# ✔️ Memory friendly
# ✔️ Lower risk
# ✖️ Sometimes less elegant

