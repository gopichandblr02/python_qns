class Solution:
    def __init__(self,data):
        self.arr=data
        self.arr_len=len(self.arr)
    def missingNumber(self):
        arr_len=len(self.arr)
        actual_arr = list(range(1,arr_len+2))
        return [x for x in actual_arr if x not in self.arr][0]

    def missingNumberSecond(self):
        my_dict=dict.fromkeys(self.arr,0)
        new_arr=list(range(1,len(self.arr)+2))
        for x in new_arr:
            if x not in my_dict:
                return x

    def arithmeticProgression(self):
        exp_sum=(self.arr_len+2)*(self.arr_len+1)//2   # // to avoid decimal format 4.0
        actual_sum=sum(self.arr)
        print(f'expected: {exp_sum} actual:{actual_sum}')
        return (exp_sum-actual_sum)

    def using_xor(self):
        xor_sum=0
        for i in range(1,self.arr_len+2):
            xor_sum=xor_sum^i
        for x in self.arr:
            xor_sum=xor_sum^x
        return xor_sum

    # ✅ 1. Best Overall Solution — XOR (O(n) time, O(1) space)
    def missingNumber(self):
        arr=self.arr+[0]
        xor = len(arr)
        for i, num in enumerate(arr):
            # xor ^= i ^ num
            xor=xor^(i^num)
        return xor
    # ✅ 2. Sum Formula (Also O(n), O(1) space)
    def missingNumberAP(self):
        n = len(self.arr)
        return (n+2) * (n + 1) // 2 - sum(self.arr)
        # If we dont have zero
        # return n * (n + 1) // 2 - sum(self.arr)


if __name__ == "__main__":
  arr = [1, 2, 3, 5]
  sol=Solution(arr)
  print(sol.missingNumber())            # 4
  print(sol.missingNumberSecond())      # 4
  print(sol.arithmeticProgression())      # 4
  print('using xor:',sol.using_xor())      # using xor: 4
  print('using xor optimized:',sol.missingNumber(),sol.missingNumber_2())      # using xor: 4
  print('AP:',sol.missingNumberAP())      # using xor: 4

  """
  Why XOR?
    -> a ^ a = 0
    -> a ^ 0 = a
    XOR cancels out duplicates.
    XOR all numbers from 0..n and XOR all elements of the array → only missing number remains.
  """

  print(4 ^ 2)
  print(2 ^ 0)
  print(2 ^ 2)
