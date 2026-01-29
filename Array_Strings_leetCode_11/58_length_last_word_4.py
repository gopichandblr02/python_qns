class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(" ")[-1])
        # return len(s.split()[-1]) This works


s=Solution()
print(s.lengthOfLastWord("luffy is still joyboy"))
print(s.lengthOfLastWord("   fly me   to   the moon  "))

# 6
# 4