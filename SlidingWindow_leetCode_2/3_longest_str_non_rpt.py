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

    def longest_nonrepeating_substring(self, s):
        start, curr_len, max_len = 0, 0, 0
        seen = {}
        for i, num in enumerate(s):
            if num in seen and i >= start:
                start = seen[num] + 1
            seen[num] = i
            curr_len = i - start + 1
            if curr_len > max_len:
                max_len = curr_len
                max_string = s[start:i + 1]
        return (max_len, max_string)

print(Solution().lengthOfLongestSubstring("abcabcbb"))
print(Solution().lengthOfLongestSubstring("bbbbb"))


sol = Solution()
# print(sol.longest_nonrepeating_substring("abcbcxyx"))
print(sol.longest_nonrepeating_substring("abccxyx"))  # (3, 'abc')
# print(sol.longest_nonrepeating_substring("abbcxyx"))   (4, 'bcxy')
# print(sol.longest_nonrepeating_substring("geeksforgeeks"))   (8, 'eeksforg')


