"""
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.
"""
class Solution():
    def isIsomorphic(self, s, t):
        s_mapper={}
        t_mapper={}
        if len(s)!=len(t):
            return False
        for x,y in zip(s,t):
            if x in s_mapper and s_mapper[x] !=y:
                return False
            if y in t_mapper and t_mapper[y] !=x:
                return False
            s_mapper[x]=y
            t_mapper[y]=x
        return True

    # check the below solution
    def isIsomorphicAnother(s: str, t: str) -> bool:
        def encode(word):
            mapping = {}
            pattern = []
            idx = 0
            for ch in word:
                if ch not in mapping:
                    mapping[ch] = idx
                    idx += 1
                pattern.append(mapping[ch])
            return pattern

        return encode(s) == encode(t)


sol = Solution()
print(sol.isIsomorphic(s = "egg", t = "add"))
print(sol.isIsomorphic(s = "foo", t = "bar"))
print(sol.isIsomorphic(s = "paper", t = "title"))
print(sol.isIsomorphic(s = "badc", t = "baba"))
