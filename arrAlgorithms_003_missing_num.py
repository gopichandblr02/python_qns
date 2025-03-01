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



if __name__ == "__main__":
  arr = [1, 2, 3, 5]
  sol=Solution(arr)
  print(sol.missingNumber())            # 4
  print(sol.missingNumberSecond())      # 4
  print(sol.arithmeticProgression())      # 4

  print('using xor:',sol.using_xor())      # using xor: 4