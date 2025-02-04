# Given a string, find the length of the longest substring without repeating characters.
# Examples:
# Given "abcabcbb", the answer is "abc", which the length is 3.
# Given "bbbbb", the answer is "b", with the length of 1.
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

#12345 string
#01234 index


class Solution:
    def lengthOfLongestSubstring(self, s):
        mapSet = {}
        start, result = 0, 0
        for end in range(len(s)):
            if s[end] in mapSet:
                start = max(mapSet[s[end]], start)
            result = max(result, end-start+1)
            mapSet[s[end]] = end+1
        return result

a = Solution()
print(f"length of longest substring without repeating characters: {a.lengthOfLongestSubstring("abcabcbb")}")