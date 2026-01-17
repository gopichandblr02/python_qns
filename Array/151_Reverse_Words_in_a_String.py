class Solution:
    def reverseWordsTemp(self, s: str) -> str:
        s =s.strip(" ")
        return ' '.join(s.split(" ")[::-1])

    def reverseWords(self, s: str) -> str:
        words = s.split()  # removes extra spaces automatically
        words.reverse()
        return " ".join(words)



s1 = "the sky is blue"
s2 = "  hello world  "
s3 = "a good   example"
# Output: "blue is sky the"
sol=Solution()
print(sol.reverseWords(s1))
print(sol.reverseWords(s2))
print(sol.reverseWords(s3))



