# Input: arr[] = [16, 17, 4, 3, 5, 2]
# Output: [17 5 2]
class Solution:
    def __init__(self,arr):
        self.arr,self.len=arr,len(arr)
    def leaders(self):
        leaders=[]
        for i in range(self.len-1):
            flag=True
            for j in range(i+1,self.len):
                if self.arr[j] > self.arr[i]:
                    flag=False
            if flag==True:
                leaders.append(self.arr[i])
        leaders.append(self.arr[-1])
        return leaders

    def leaders_optimal(self):
        right_most = self.arr[-1]
        leaders = [right_most]
        for i in range(self.len-2,-1,-1):
            if right_most < self.arr[i]:
                leaders.append(self.arr[i])
            right_most = max(right_most,self.arr[i])
        return list(reversed(leaders))

arr=[16, 17, 4, 3, 5, 2]
sol=Solution(arr)
print(sol.leaders()) # [17, 5, 2]
print(sol.leaders_optimal())  # [17, 5, 2]