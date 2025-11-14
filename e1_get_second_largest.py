class Solution:
    def getSecondLargest(self,arr):
        arr_len=len(arr)
        arr.sort()

        for i in range(arr_len-2,-1,-1):
            if arr[i]!=arr[arr_len-1]:
                return arr[i]

arr = [12, 35, 1, 10, 34, 1]
print(Solution().getSecondLargest(arr))