class Solution:
    def wordBreak(self, s, wordDict):
        pass



sol=Solution()
print(sol.wordBreak(s = "leetcode", wordDict = ["leet","code"]))
# true
print(sol.wordBreak(s = "applepenapple", wordDict = ["apple","pen"]))
# true
print(sol.wordBreak(s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]))
# false