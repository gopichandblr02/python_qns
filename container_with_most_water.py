# Time:  O(n)
# Space: O(1)

a =[1,8,6,2,5,4,8,3,7]
a1=[1,100,1,102]

class Solution(object):
    def area_max(self,arr):
        area,i=0,0
        j=len(arr)-1
        while i<j:
            area = max(area,min(arr[i],arr[j])*(j-i))
            if arr[i] < arr[j]:
                i+=1
            else:
                j-=1
        return area

sol = Solution()
print(sol.area_max(a1))

