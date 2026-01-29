class Solution:
    def plusOne(self, digits):
        return list(map(int, list(str(int(''.join(map(str, digits))) + 1))))

# Example usage:
sol = Solution()
print(sol.plusOne([1,2,3]))  # Output: [1,2,4]
print(sol.plusOne([4,3,2,1]))  # Output: [4,3,2,2]
print(sol.plusOne([9]))  # Output: [1,0]
