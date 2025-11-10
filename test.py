arr=[16, 17, 4, 3, 5, 2]

a = arr[-1:0:-1]
print(a)



# arr_len = len(arr)
# for x in range(1,arr_len):
#     print(arr[x])
#
# for x in arr[1:]:
#     print(x)


# arr=[16, 17, 4, 3, 5, 2]
# arr_len = len(arr)
# for i in range(arr_len-2,-1,-1):
#     print(arr[i])

# class Solution:
#     def func(self,strs):
#         pref = strs[0]
#         for x in strs[1:]:
#             while not x.startswith(pref):
#                 pref = pref[:-1]
#         return pref
#
#
# strs = ["flower","flow","flight"]
# sol = Solution()
# print(sol.func(strs))

# a=[1]+[2,4]
# print(a)
#
#
# x="1251"
#
# print(sorted(x))