class Solution:
    def __init__(self,arr,k):
        self.arr,self.k=arr,k
    def smallest_largest(self):
        self.arr.sort()
        print(self.arr)
        return (self.arr[self.k-1],self.arr[-self.k])

arr = [12, 3, 5, 7, 19, 1]
k = 2
sol=Solution(arr,k)
print(f"{k}th smallest element: {sol.smallest_largest()[0]}")
print(f"{k}th largest element: {sol.smallest_largest()[1]}")