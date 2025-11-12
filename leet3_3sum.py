from itertools import combinations

arr=[-1,0,1,2,-1,-4]
arr1=[0,2,-2,3,-3]

class Solution:
    def three_sum_sol(self,arr):
        arr.sort()
        n=len(arr)
        res=[]
        for i in range(n-2):
            # since we can deal with arr[i-1] and arr[i] is no longer needed; as both ae same
            if i>0 and arr[i]==arr[i-1]:
                continue
            left=i+1
            right=n-1
            while left<right:
                s=arr[i]+arr[left]+arr[right]
                if s==0:
                    res.append([arr[i],arr[left],arr[right]])
                    left+=1
                    right-=1
                    # skip duplicates for left and right
                    while left<right and arr[left]==arr[left-1]:
                        left+=1
                    while left<right and arr[right]==arr[right+1]:
                        right-=1
                elif s<0:
                    left += 1
                else:
                    right -= 1
        return res

    # This is slow compared to above solution
    # The number of triplets is O(n³) — because it checks every combination of 3 numbers from n.
    # Each triplet’s sum must be computed and checked — still O(1), but the total count makes it O(n³)
    # Also, you need to remove duplicates manually → adds even more overhead.
    def my_3sum_sol(self,arr):
        arr_combs=[sorted(list(c)) for c in combinations(arr,3) if sum(c)==0]
        final_list = []
        for x in arr_combs:
            if x in final_list:
                continue
            else:
                final_list.append(x)
        return final_list

print(Solution().three_sum_sol(arr))
print(Solution().three_sum_sol(arr1))
# print(Solution().my_3sum_sol(arr))