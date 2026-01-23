"""
string_coding_solutions.py

Solutions for Top 50 String Coding Problems for Interviews (GeeksforGeeks).
Last Updated : 18 Sep, 2025
URL: https://www.geeksforgeeks.org/dsa/top-50-string-coding-problems-for-interviews/
"""

import re
import string
from collections import Counter, defaultdict, deque
from functools import lru_cache

# ---------------------------- EASY PROBLEMS ----------------------------

# 1. Palindrome Check
def is_palindrome(s: str) -> bool:
    return s == s[::-1]

# 2. Reverse a String
def reverse_string(s: str) -> str:
    return s[::-1]

# 3. Reverse Words in a Sentence
def reverse_words(sentence: str) -> str:
    return " ".join(sentence.split()[::-1])

# 4. Check for Rotation
def is_rotation(s1: str, s2: str) -> bool:
    return len(s1) == len(s2) and s2 in (s1 + s1)

# 5. First Non Repeating Character
def first_non_repeating_char(s: str) -> str:
    freq = Counter(s)
    for ch in s:
        if freq[ch] == 1:
            return ch
    return ""

# 6. Roman to Integer
def roman_to_int(s: str) -> int:
    vals = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    total = 0
    prev = 0
    for ch in reversed(s):
        if vals[ch] < prev:
            total -= vals[ch]
        else:
            total += vals[ch]
        prev = vals[ch]
    return total

# 7. Implement Atoi (string to int)
def my_atoi(s: str) -> int:
    s = s.strip()
    if not s:
        return 0
    sign = 1
    i = 0
    if s[0] in ('+','-'):
        sign = 1 - 2*(s[0]=='-')
        i += 1
    num = 0
    while i < len(s) and s[i].isdigit():
        num = num*10 + (ord(s[i]) - ord('0'))
        i += 1
    return sign*num

# 8. Encrypt the String – II (simple Caesar shift)
def encrypt_string(s: str, shift: int=3) -> str:
    result = []
    for ch in s:
        if ch.isalpha():
            base = 'A' if ch.isupper() else 'a'
            result.append(chr((ord(ch)-ord(base)+shift)%26 + ord(base)))
        else:
            result.append(ch)
    return "".join(result)

# 9. Equal Point in Brackets (count matches)
def equal_point_in_brackets(s: str) -> int:
    count = 0
    eq = 0
    for ch in s:
        if ch == '(':
            eq = 0
        if ch == '=':
            eq += 1
        if ch == ')':
            if eq > 0:
                count += 1
    return count

# 10. Anagram Checking
def are_anagrams(s1: str, s2: str) -> bool:
    return Counter(s1) == Counter(s2)

# 11. Panagram Checking
def is_pangram(s: str) -> bool:
    return set(string.ascii_lowercase).issubset(set(s.lower()))

# 12. Validate IP Address
def validate_ip(ip: str) -> bool:
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for p in parts:
        if not p.isdigit() or not 0 <= int(p) <= 255 or (p[0]=='0' and len(p)>1):
            return False
    return True

# 13. Add Binary Strings
def add_binary(a: str, b: str) -> str:
    return bin(int(a,2) + int(b,2))[2:]

# -------------------------- MEDIUM PROBLEMS --------------------------

# 14. Integer to Words
def int_to_words(num: int) -> str:
    # Basic implementation for positive ints
    under20 = ["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine",
               "Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen",
               "Seventeen","Eighteen","Nineteen"]
    tens = ["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
    def helper(n):
        if n < 20:
            return under20[n]
        if n < 100:
            return tens[n//10] + ('' if n%10==0 else ' ' + under20[n%10])
        if n < 1000:
            return under20[n//100] + ' Hundred' + ('' if n%100==0 else ' ' + helper(n%100))
        for p, w in [(10**9,"Billion"),(10**6,"Million"),(10**3,"Thousand")]:
            if n >= p:
                return helper(n//p) + ' ' + w + ('' if n%p==0 else ' ' + helper(n%p))
    return helper(num)

# 15. Fizz Buzz
def fizz_buzz(n: int) -> list[str]:
    result = []
    for i in range(1, n+1):
        if i%15==0:
            result.append("FizzBuzz")
        elif i%3==0:
            result.append("Fizz")
        elif i%5==0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

# 16. Palindromic Sentence Check
def palindromic_sentence(s: str) -> bool:
    t = ''.join(ch.lower() for ch in s if ch.isalnum())
    return t == t[::-1]

# 17. Isomorphic Strings
def is_isomorphic(s1: str, s2: str) -> bool:
    return (len(s1)==len(s2) and
            len(set(zip(s1,s2))) == len(set(s1)) == len(set(s2)))

# 18. Check for k-anagram
def is_k_anagram(s1: str, s2: str, k: int) -> bool:
    if len(s1) != len(s2):
        return False
    diff = 0
    c1, c2 = Counter(s1), Counter(s2)
    for ch in c1:
        if c1[ch] > c2[ch]:
            diff += c1[ch]-c2[ch]
    return diff <= k

# 19. Equal 0,1, and 2 (balanced)
def equal_012(s: str) -> bool:
    return Counter(s)['0'] == Counter(s)['1'] == Counter(s)['2']

# 20. Find and replace in String
def find_and_replace(s: str, old: str, new: str) -> str:
    return s.replace(old, new)

# 21. Look and Say Pattern
def look_and_say(n: int) -> str:
    s = "1"
    for _ in range(n-1):
        prev = s
        s = ""
        i = 0
        while i < len(prev):
            count = 1
            while i+1 < len(prev) and prev[i]==prev[i+1]:
                i+=1
                count+=1
            s += str(count)+prev[i]
            i+=1
    return s

# 22. Minimum repetitions to make Substring
def min_reps_to_contain(a: str, b: str) -> int:
    reps = -(-len(b) // len(a))  # ceil
    s = a * reps
    if b in s:
        return reps
    if b in s + a:
        return reps+1
    return -1

# 23. Excel Sheet – I (convert number to column title)
def excel_col_title(n: int) -> str:
    res = ""
    while n:
        n -= 1
        res = chr(n%26 + ord('A')) + res
        n //= 26
    return res

# 24. Find the N-th character (in repeated string)
def find_nth_char(s: str, n: int) -> str:
    return s[(n-1) % len(s)]

# 25. Next Palindromic Number
def next_palindromic_number(num: str) -> str:
    n = len(num)
    left = num[:(n+1)//2]
    candidate = left + left[:n//2][::-1]
    if candidate > num:
        return candidate
    left_as_num = str(int(left) + 1)
    return left_as_num + left_as_num[:n//2][::-1]

# ... (CONTINUED in next message due to size) ...
