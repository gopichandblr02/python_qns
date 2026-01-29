class Solution:
    # avoid below solution
    #     Uses big integers
    #     Ignores core logic
    #     Language - dependent

    def plusOne(self, digits):
        return list(map(int, list(str(int(''.join(map(str, digits))) + 1))))

    # ⏱ Time & Space Complexity
    # Time: O(n) (Worst case: all digits are 9)
    # Space: O(1) (Ignoring output array)

    def plusOneOptimal(self, digits):
        n = len(digits)
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        # If we are here, all digits were 9
        return [1] + digits

# Example usage:
sol = Solution()
print(sol.plusOne([1,2,3]))  # Output: [1,2,4]
print(sol.plusOne([4,3,2,1]))  # Output: [4,3,2,2]
print(sol.plusOne([9]))  # Output: [1,0]

print(sol.plusOneOptimal([1,2,3]))  # Output: [1,2,4]
print(sol.plusOneOptimal([4,3,2,1]))  # Output: [4,3,2,2]
print(sol.plusOneOptimal([9]))  # Output: [1,0]
print(sol.plusOneOptimal([9,9]))  # Output: [1,0,0]
