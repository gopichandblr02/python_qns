"""
Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter.
"""

class Solution:
    def wordPattern(self, pattern, s):
        s=s.split(" ")
        p_mapper={}
        s_mapper={}
        if len(pattern)!=len(s):
            return False
        for x,y in zip(pattern,s):
            if x in p_mapper and p_mapper[x]!=y:
                return False
            if y in s_mapper and s_mapper[y]!=x:
                return False
            p_mapper[x]=y
            s_mapper[y]=x
        return True

sol=Solution()

print(sol.wordPattern(pattern = "abba", s = "dog cat cat dog"))
print(sol.wordPattern(pattern = "abba", s = "dog cat cat fish"))
print(sol.wordPattern(pattern = "aaaa", s = "dog cat cat dog"))
