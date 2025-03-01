class Solution:
    def __init__(self,arr,k):
        self.arr=arr
        self.k=k

    def rotate(self):
        self.k%=len(self.arr)
        return self.arr[-self.k:]+self.arr[:-self.k]

arr=[1,2,3,4,5,6,7,8]
k=3
sol = Solution(arr,k)
print(sol.rotate())
