class Solution:
    def plusOne(self, digits):
        return list(map(int,list(str(int(''.join(map(str,digits)))+1))))
    def plusOne_another(self, digits):
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0  # carry-over
        # If all digits were 9, we get something like 999 → 000 → add 1 at front
        return [1] + digits
print(Solution().plusOne([9,9]))            # [1, 0, 0]
print(Solution().plusOne_another([9,9]))    # [1, 0, 0]
print(Solution().plusOne_another([8,9]))    # [9, 0]
print(Solution().plusOne_another([8,8]))    # [8, 9]

# Basics
a=[1,2,3]
# TypeError: sequence item 0: expected str instance, int found
# b=''.join(a)
# print(b)
c=''.join(map(str,a))
print(c)   # 123

number = 67890
list_of_digits = list(map(int, str(number)))
print(list_of_digits)
# Output: [6, 7, 8, 9, 0]

