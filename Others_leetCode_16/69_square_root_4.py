class Solution:
    def mySqrt(self,x):
        if x<2:
            return x
        left,right=1,x//2
        while left<=right:
            mid = (left+right)//2
            sq=mid*mid
            if sq == x:
                return mid
            elif sq<x:
                left=mid+1
            else:
                right=mid-1
        return right

s=Solution()
# print(s.mySqrt(8))  # Output: 2
# print(s.mySqrt(16)) # Output: 4
print(s.mySqrt(9)) # Output: 3
print(s.mySqrt(10)) # Output: 3

