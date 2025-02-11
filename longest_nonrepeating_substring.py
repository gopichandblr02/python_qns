class Solution:
    def longest_nonrepeating_substring(self,s):
        start, curr_len, max_len=0,0,0
        seen={}
        for i,num in enumerate(s):
            if num in seen and i>=start:
                start=seen[num]+1
            seen[num]=i
            curr_len=i-start+1
            if curr_len>max_len:
                max_len=curr_len
                max_string=s[start:i+1]
        return (max_len,max_string)
sol = Solution()
# print(sol.longest_nonrepeating_substring("abcbcxyx"))
print(sol.longest_nonrepeating_substring("abccxyx"))  # (3, 'abc')
# print(sol.longest_nonrepeating_substring("abbcxyx"))   (4, 'bcxy')
# print(sol.longest_nonrepeating_substring("geeksforgeeks"))   (8, 'eeksforg')





