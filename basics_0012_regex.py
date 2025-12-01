import re

"""
This means:
Find all characters NOT in this allowed set:
    a–z
    A–Z
    0–9
space " "
Replace each such character with a space (' ') or ''.
"""
s="A man, a plan, a canal: Panama"
print(s)
s=re.sub(r'[^a-zA-Z0-9]', '', s)
print(s)

