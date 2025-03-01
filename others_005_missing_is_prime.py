import math
class Solution:
    def __init__(self,arr):
        self.arr=arr
        self.len=len(arr)
    def find_missing(self):
        actual_sum=sum(self.arr)
        expected_sum=(self.len+1)*(self.len+2)//2
        missing_num = expected_sum-actual_sum
        return (missing_num,self.is_prime(missing_num))

    def is_prime(self,num):
        if num <=3:
            return num>1
        if num%2==0 or num%3==0:
            return False
        for i in range(5,int(math.sqrt(self.len)),6):
            if num%i==0 or num%(i+2):
                return False
        return True

a=[1,2,3,4,5,6,8]
b=[1,3,4,5,6]
c=[1,2,4,5]
d=[1,2,3,5,6,7]

print(Solution(a).find_missing())
print(Solution(b).find_missing())
print(Solution(c).find_missing())
print(Solution(d).find_missing())
