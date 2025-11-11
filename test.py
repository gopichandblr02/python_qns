class Solution:
    flag = -1 if x < 0 else 1
    x = abs(x)
    y = 0
    while x:
        y = y * 10 + int(x % 10)
        x = x // 10
    return y * flag

sol=Solution()
print(sol.reverse(123))



# a=[1,2,5,3]
# b=reversed(a)
# c=sorted(a)
# print(b)
# print(c,''.join(map(str,c)))


# 1;2;3



# class Solution:
#     def __init__(self,arr):
#         self.arr,self.len=arr,len(arr)
#     def leaders_optimal(self):
#         right_most =self.arr[-1]
#         leaders = [right_most]
#         for i in range(self.len-2,-1,-1):
#             if self.arr[i]>right_most:
#                 leaders.append(self.arr[i])
#             right_most = max(right_most,self.arr[i])
#         return list(reversed(leaders))
#
# arr=[16, 17, 4, 3, 5, 2]
# sol=Solution(arr)
# print(sol.leaders_optimal())  # [17, 5, 2]

# arr=[16, 17, 4, 3, 5, 2]
#
# a = arr[-1:0:-1]
# print(a)



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