'''
	Given a string, find the length of the longest substring without repeating characters.

	Examples:

	Given "abcabcbb", the answer is "abc", which the length is 3.

	Given "bbbbb", the answer is "b", with the length of 1.

	Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapSet={}
        start,result=0
        for i,x in enumerate(s):
            if x in mapSet:
                start=max(start,mapSet[x])
            result=max(result,i-start+1)
            mapSet[x]=i+1
        return result


print(Solution().lengthOfLongestSubstring("abcabcbb"))
print(Solution().lengthOfLongestSubstring("bbbbb"))