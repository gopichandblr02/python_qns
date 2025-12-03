import re

"""
| Function        | Purpose                                  |
| --------------- | ---------------------------------------- |
| `re.search()`   | Finds first match anywhere in the string |
| `re.match()`    | Matches only at the beginning            |
| `re.findall()`  | Returns *all* matches as a list          |
| `re.finditer()` | Returns an iterator of match objects     |
| `re.sub()`      | Replace text that matches a pattern      |
| `re.split()`    | Split a string using regex               |
"""






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

"""[^ ... ]
[] → character class (a set of allowed characters)
^ inside the brackets → negation (“NOT these characters”)"""

s = "Hello 123 World_! Regex-99"
re.findall(r'\d', s)
['1', '2', '3', '9', '9']

re.findall(r'\D', s)

