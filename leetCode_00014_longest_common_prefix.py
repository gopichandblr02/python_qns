class Solution:
    def func(self,strs):
        pref = strs[0]
        for x in strs[1:]:
            while not x.startswith(pref):
                pref = pref[:-1]
                if not pref:
                    return ""
        return pref


strs = ["flower","flow","flight"]
sol = Solution()
print(sol.func(strs))
# fl