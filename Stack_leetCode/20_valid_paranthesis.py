def isValid(s: str) -> bool:
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for ch in s:
        if ch in mapping:
            if not stack or stack[-1] != mapping[ch]:
                return False
            stack.pop()
        else:
            stack.append(ch)

    return not stack

s22=")"
print(isValid(s22))
# False

s2="([)]"
print(isValid(s2))
# False

s0 = "{"
print(isValid(s0))
# False
s = "{[()]}"
print(isValid(s))
# True
s1 = "{[()]"
print(isValid(s1))
# False