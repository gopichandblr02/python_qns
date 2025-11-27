class Solution:
    def reverse(self, x):
        flag=-1 if x<0 else 1
        x =abs(x)
        y=0
        while x:
            y=y*10+int(x%10)
            x=x//10
        rev = y*flag
        if rev >= (-2**31) and rev <= (2**31-1):
            return rev
        else:
            return 0

    def reverse_way2(self, x):
        flag=-1 if x<0 else 1
        x=x*flag
        rev=int(str(x)[::-1])*flag
        if rev >= (-2**31) and rev <= (2**31-1):
            return rev
        else:
            return 0


sol=Solution()
print(sol.reverse(123))
print(sol.reverse_way2(123))
print(sol.reverse(-1234))
print(sol.reverse_way2(-1235))
