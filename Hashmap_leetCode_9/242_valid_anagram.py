class Solution:
    def isAnagram(self, s, t):
        if ''.join(sorted(s)) ==''.join(sorted(t)):
            return True
        else:
            return False

s = "anagram"
t = "nagaram"
sol = Solution()
print(sol.isAnagram(s, t))
# Output: true

s1 = "rat"
t1 = "car"
print(sol.isAnagram(s1, t1))
# Output: false

