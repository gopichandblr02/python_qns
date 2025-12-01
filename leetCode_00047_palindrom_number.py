import re

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        else:
            st = str(x)
            i=0
            end=len(st)
            check=(len(st)//2)-1
            while i <=check:
                if st[i]==st[end-i-1]:
                    i+=1
                elif st[i]!=st[end-i-1]:
                    return False
            return True

    def is_Palindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9 ]', ' ', s).replace(" ","").lower()
        i=0
        end=len(s)
        check=(len(s)//2)-1
        while i <=check:
            if s[i]==s[end-i-1]:
                i+=1
            elif s[i]!=s[end-i-1]:
                return False
        return True


print(Solution().isPalindrome(121))
print(Solution().isPalindrome(1221))
print(Solution().isPalindrome(-121))
print(Solution().isPalindrome(10))

print(Solution().is_Palindrome("A man, a plan, a canal: Panama"))

