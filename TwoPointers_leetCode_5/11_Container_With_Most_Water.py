class Solution:
    def maxArea(self, arr):
        area, i = 0, 0
        j = len(arr) - 1
        while i < j:
            area = max(area, min(arr[i], arr[j]) * (j - i))
            if arr[i] < arr[j]:
                i += 1
            else:
                j -= 1
        return area

height = [1,8,6,2,5,4,8,3,7]
sol = Solution()
print(sol.area_max(height))

# Output: 49