class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(" ")[-1])


s=Solution()
print(s.lengthOfLastWord("luffy is still joyboy"))
print(s.lengthOfLastWord("   fly me   to   the moon  "))

# 6
# 4