import math
from pickletools import read_stringnl_noescape


class Solution:
    def __init__(self,num):
        self.num=num
    def traditional(self):
        for i in range(2,self.num):
            if self.num%i==0:
                return 'Not Prime'
            else:
                return 'Prime'
    def num_half(self):
        for i in range(2,(self.num//2)+1):
            if self.num%i==0:
                return 'Not Prime'
            else:
                return 'Prime'
    def square_root(self):
        for i in range(2,int(math.sqrt(self.num))+1):   #plus 1 to include upper bound
            if self.num%i==0:
                return 'Not Prime'
            else:
                return 'Prime'

    def square_root_recursion(self,iter):
        pass

    # Any number -> 6k, 6k+1, k_2, 6k+3, 6k+4, 6k+5
    # any prime number can be expressed as 6k+-1
    # Any composite number can be written as product of prime numbers
    def square_root_fewer_checks(self):
        if self.num<=3:
            return self.num>1
        if self.num%2==0 or self.num%3==0:
            return False
        for i in range(5,int(math.sqrt(self.num))+1,6):
            if self.num%i==0 or self.num%(i+2)==0:
                return False
        return True

print(Solution(23).traditional())  # Prime
print(Solution(22).traditional()) # Not Prime
print(Solution(23).num_half()) # Prime
print(Solution(22).num_half()) # Not Prime
print(Solution(23).square_root()) # Prime
print(Solution(22).square_root()) # Not Prime
print(Solution(41).square_root_fewer_checks()) # Prime
print(Solution(22).square_root_fewer_checks()) # Not Prime

# Using recursion
print(Solution(23).square_root_recursion(int(math.sqrt(23)))) # Prime
print(Solution(22).square_root_recursion(int(math.sqrt(22)))) # Not Prime