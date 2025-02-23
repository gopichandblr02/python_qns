numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

class Solution:
    def __init__(self,arr):
        self.arr = arr
        self.arr_len = len(arr)

    def two_loops(self):
        max_sum = self.arr[0]
        for i in range(self.arr_len):
            for j in range(i,self.arr_len):
                max_sum = max(max_sum,sum(self.arr[i:j]))

        return max_sum
    def single_loop(self):
        max_sum = float('-inf')
        cur_sum=0
        for x in self.arr:
            cur_sum = max(x,x+cur_sum)
            max_sum = max(max_sum,cur_sum)
        return max_sum

sol = Solution(numbers)

print("two loops: ",sol.two_loops(),"single loop:",sol.single_loop())
# two loops:  6 single loop: 6