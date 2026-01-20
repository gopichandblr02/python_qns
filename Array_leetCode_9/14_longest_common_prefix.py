class Solution:
    def func(self,strs):
        pref = strs[0]
        for x in strs[1:]:
            while not x.startswith(pref):
                pref = pref[:-1]
                if not pref:
                    return   # same as return None
        return pref


strs = ["flower","flow","flight"]
strs1 = ["flower","aa","cc"]
sol = Solution()
print(sol.func(strs)) # fl
print(sol.func(strs1)) # None
