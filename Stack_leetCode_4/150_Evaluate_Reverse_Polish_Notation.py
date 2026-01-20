"""
Which matches LeetCode requirement: truncate toward zero.
-3 / 2 = -1.5 → int(-1.5) = -1
"""


class Solution:
    def evalRPN(self, tokens):
        stack = []

        for t in tokens:
            if t in "+-*/":
                b = stack.pop()
                a = stack.pop()

                if t == "+":
                    stack.append(a + b)
                elif t == "-":
                    stack.append(a - b)
                elif t == "*":
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))   # truncate toward zero
            else:
                stack.append(int(t))

        return stack[0]
# Example usage:
sol = Solution()
# print(sol.evalRPN(["2", "1", "+", "3", "*"]))
# Output: 9
print(sol.evalRPN(["4","13","5","/","+"]))
# Output: 6

"""
13 / 5 = 2
4 + 2 = 6

Always remember:
Second pop = right operand
Wrong order = wrong answer.
"""


