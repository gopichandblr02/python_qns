class Solution:
    def func(self,a):
        sign_flag= -1 if a<0 else 1
        val = str(abs(a))
        return (sign_flag)*int(val[::-1])

    def func2(self,a):
        ans =0
        sign_flag= -1 if a<0 else 1
        a=sign_flag*a
        while a:
            ans = ans*10+a%10
            a=a//10
        return 0 if (ans< -2**31 or ans>2**31) else sign_flag*ans
sol = Solution()
print(sol.func(-123)) # -321
print(sol.func(189)) # 981
print(sol.func2(-189)) # -981
print(sol.func2(123)) # 321