# Python Regex Special Sequences Explained (`\d`, `\w`, `\s`, etc.)

This guide explains the most commonly used **Python regular expression special sequences** with clear definitions and examples.

---

## 1. `\d` — Digit  
Matches **any digit** from `0–9`.

### Example
```python
import re
print(re.findall(r"\d", "Room 123B"))    # ['1', '2', '3']
```

---

## 2. `\D` — Non‑digit  
Matches **any character that is NOT a digit**.

### Example
```python
print(re.findall(r"\D", "A9$@3"))   # ['A', '$', '@']
```

---

## 3. `\w` — Word Character  
Matches **alphanumeric characters** and underscore:  
`A–Z`, `a–z`, `0–9`, `_`

### Example
```python
print(re.findall(r"\w", "Hi_123!!"))   # ['H','i','_','1','2','3']
```

---

## 4. `\W` — Non‑word Character  
Matches **everything EXCEPT** letters, digits, and underscore.

### Example
```python
print(re.findall(r"\W", "Hi_123!!"))   # ['!','!']
```

---

## 5. `\s` — Whitespace  
Matches **spaces, tabs, newlines** (`" "`, `\t`, `\n`).

### Example
```python
print(re.findall(r"\s", "Hello World\nHi"))   
# [' ', '\n']
```

---

## 6. `\S` — Non‑Whitespace  
Matches all characters **except spaces, tabs, newlines**.

### Example
```python
print(re.findall(r"\S", "A B\tC"))   # ['A','B','C']
```

---

## 7. `\b` — Word Boundary  
Matches the **boundary between a word and a non‑word character**.

Useful for matching whole words.

### Example
```python
print(re.findall(r"\bcat\b", "cat scatter category cat"))  
# ['cat']
```

---

## 8. `\B` — Non‑Boundary  
Matches locations **NOT at a word boundary**.

### Example
```python
print(re.findall(r"\Bcat\B", "concatenate category cat"))  
# ['cat']  # only inside words
```

---

## 9. `\A` — Match Start of String Only  
Matches only at the **very beginning** of the input.

### Example
```python
print(re.findall(r"\AHello", "Hello World Hello"))  
# ['Hello']
```

---

## 10. `\Z` — Match End of String Only  
Matches only at the **very end** of the input.

### Example
```python
print(re.findall(r"World\Z", "Hello World"))  
# ['World']
```

---

## 11. `\G` — Continuous Match (Rarely Used)  
Matches **where the last match ended**.  
Not commonly used in simple patterns.

---

## Summary Table

| Sequence | Meaning |
|----------|---------|
| `\d` | Digit (0–9) |
| `\D` | Non-digit |
| `\w` | Word char (letters, digits, `_`) |
| `\W` | Non‑word char |
| `\s` | Whitespace |
| `\S` | Non‑whitespace |
| `\b` | Word boundary |
| `\B` | Non‑word boundary |
| `\A` | Start of string |
| `\Z` | End of string |
| `\G` | Last match end |

---

########################################################################

# Python Regex (re) --- Complete Guide with Full Explanations & Examples

This is a complete, well‑structured Markdown guide covering **all
essential Python regex topics**, each with explanations and examples.

------------------------------------------------------------------------

## 1. Introduction

Python provides regular expression support through the built‑in `re`
module.

``` python
import re
```

------------------------------------------------------------------------

# 2. Core Regex Functions

## 2.1 `re.search(pattern, string)`

Finds the **first match anywhere** in the string.

``` python
m = re.search(r"dog", "I love my dog and another dog")
print(m.group())  
# dog
```

------------------------------------------------------------------------

## 2.2 `re.match(pattern, string)`

Matches **at the beginning** of the string.

``` python
m = re.match(r"Hello", "Hello World")
print(m.group())
# Hello
```

------------------------------------------------------------------------

## 2.3 `re.fullmatch(pattern, string)`

Requires the **entire string** to match.

``` python
re.fullmatch(r"\d+", "12345")   # valid
re.fullmatch(r"\d+", "123a")    # None
```

------------------------------------------------------------------------

## 2.4 `re.findall(pattern, string)`

Returns **all occurrences** as a list.

``` python
re.findall(r"\d+", "A1 B22 C333")
# ['1', '22', '333']
```

------------------------------------------------------------------------

## 2.5 `re.finditer(pattern, string)`

Same as `findall` but returns **iterators** with match objects.

``` python
for m in re.finditer(r"\d+", "A1 B22 C333"):
    print(m.group(), m.start(), m.end())
```

------------------------------------------------------------------------

## 2.6 `re.sub(pattern, replacement, string)`

Replaces all matches.

``` python
clean = re.sub(r"[^a-zA-Z0-9 ]", " ", "Hello!! Welcome...")
# 'Hello   Welcome   '
```

------------------------------------------------------------------------

## 2.7 `re.split(pattern, string)`

Splits based on regex.

``` python
re.split(r"\s+", "Python   is   great")
# ['Python', 'is', 'great']
```

------------------------------------------------------------------------

## 2.8 `re.compile(pattern)`

Compiles a regex for reuse (faster).

``` python
pattern = re.compile(r"\d+")
pattern.findall("a1 b22 c333")
```

------------------------------------------------------------------------

# 3. Regex Metacharacters

## 3.1 Dot `.`

Matches any character except newline.

``` python
re.findall(r"h.t", "hat hot hit h t")
# ['hat', 'hot', 'hit']
```

------------------------------------------------------------------------

# 4. Character Classes & Sets

## 4.1 `[ ]` --- Match any character from the set

``` python
re.findall(r"[aeiou]", "hello")
# ['e','o']
```

------------------------------------------------------------------------

## 4.2 `[^ ]` --- Negated character set

Matches any character **not** listed.

``` python
re.findall(r"[^0-9]", "a1b2c3")
# ['a', 'b', 'c']
```

------------------------------------------------------------------------

## 4.3 Ranges

``` python
re.findall(r"[A-Z]", "AbCdeF")
# ['A','C','F']
```

------------------------------------------------------------------------

# 5. Predefined Character Classes

  Pattern   Meaning
  --------- ---------------------------------
  `\d`      digit
  `\D`      non‑digit
  `\w`      word char (letters, digits, \_)
  `\W`      non-word
  `\s`      whitespace
  `\S`      non-whitespace

------------------------------------------------------------------------

### Examples

``` python
re.findall(r"\d", "a1b2c3")  
# ['1', '2', '3']

re.findall(r"\w+", "Hi_123!")
# ['Hi_123']
```

------------------------------------------------------------------------

# 6. Anchors (Position Matchers)

## 6.1 `^` --- Start of string

``` python
re.match(r"^Hello", "Hello World")
```

------------------------------------------------------------------------

## 6.2 `$` --- End of string

``` python
re.search(r"world$", "Hello world")
```

------------------------------------------------------------------------

## 6.3 `\b` --- Word boundary

``` python
re.findall(r"\bcat\b", "cat scatter cater")
# ['cat']
```

------------------------------------------------------------------------

## 6.4 `\B` --- Not a word boundary

``` python
re.findall(r"\Bcat", "scatter cater cat")
# ['cat', 'cat']
```

------------------------------------------------------------------------

# 7. Quantifiers

  Pattern    Meaning
  ---------- -----------
  `a*`       0 or more
  `a+`       1 or more
  `a?`       0 or 1
  `a{3}`     exactly 3
  `a{2,4}`   2--4
  `a{2,}`    2 or more

### Example

``` python
re.findall(r"ha+", "ha haa haaa")
# ['ha', 'haa', 'haaa']
```

------------------------------------------------------------------------

# 8. Grouping

## 8.1 Capturing Groups `()`

``` python
m = re.search(r"(\w+)@(\w+)", "email test@gmail")
print(m.group(1))  # test
print(m.group(2))  # gmail
```

------------------------------------------------------------------------

## 8.2 Non‑Capturing Groups `(?: )`

``` python
re.findall(r"(?:ha)+", "hahaha")
# ['hahaha']
```

------------------------------------------------------------------------

## 8.3 Named Groups

``` python
m = re.search(r"(?P<name>\w+) (?P<age>\d+)", "John 30")
print(m.group("name"))  # John
print(m.group("age"))   # 30
```

------------------------------------------------------------------------

# 9. Alternation (OR)

``` python
re.findall(r"cat|dog", "cat dog frog")
# ['cat','dog']
```

------------------------------------------------------------------------

# 10. Lookarounds (Advanced)

## 10.1 Positive Lookahead `(?= )`

``` python
re.findall(r"\w+(?=\.)", "hello.world test")
# ['hello']
```

------------------------------------------------------------------------

## 10.2 Negative Lookahead `(?! )`

``` python
re.findall(r"hello(?! world)", "hello hi hello world")
# ['hello']
```

------------------------------------------------------------------------

## 10.3 Positive Lookbehind `(?<= )`

``` python
re.findall(r"(?<=\$)\d+", "$50 and $70")
# ['50', '70']
```

------------------------------------------------------------------------

## 10.4 Negative Lookbehind `(?<! )`

``` python
re.findall(r"(?<!\$)\d+", "50 $60 70")
# ['50', '70']
```

------------------------------------------------------------------------

# 11. Escaping Special Characters

``` python
re.findall(r"\.", "a.b.c")
# ['.','.']
```

------------------------------------------------------------------------

# 12. Regex Flags

  Flag     Meaning
  -------- ---------------------------
  `re.I`   Ignore case
  `re.M`   \^ and \$ match each line
  `re.S`   Dot matches newline
  `re.X`   Verbose mode

------------------------------------------------------------------------

### Ignore case example

``` python
re.findall(r"hello", "Hello hELLo", re.I)
# ['Hello','hELLo']
```

------------------------------------------------------------------------

### Dot matches newline example

``` python
re.findall(r".+", "a\nb", re.S)
# ['a\nb']
```

------------------------------------------------------------------------

# 13. Practical Real‑World Examples

## 13.1 Extract emails

``` python
re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[A-Za-z]{2,}", text)
```

------------------------------------------------------------------------

## 13.2 Extract phone numbers

``` python
re.findall(r"\d{3}-\d{3}-\d{\4}", "Call 123-456-7890")
```

------------------------------------------------------------------------

## 13.3 Validate strong password

``` python
re.fullmatch(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$", "Test1234")
```

------------------------------------------------------------------------

## 13.4 Remove special characters

``` python
re.sub(r"[^a-zA-Z0-9 ]", "", "Hello!!@# World")
# Hello World
```

------------------------------------------------------------------------

## 13.5 Extract hashtags

``` python
re.findall(r"#\w+", "I love #python and #regex")
# ['#python', '#regex']
```

------------------------------------------------------------------------

## 13.6 Split on commas, semicolons & spaces

``` python
re.split(r"[ ,;]+", "a, b; c  d")
# ['a','b','c','d']
```

------------------------------------------------------------------------

# END OF GUIDE
