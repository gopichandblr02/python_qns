"""
    Given an array A of strings made only from lowercase letters, return a
    list of all characters that show up in all strings within the list
    (including duplicates).  For example, if a character occurs 3 times in
    all strings but not 4 times, you need to include that character three
    times in the final answer.

    You may return the answer in any order.

    Example:
    Input: ["bella","label","roller"]
    Output: ["e","l","l"]

    Example:
    Input: ["cool","lock","cook"]
    Output: ["c","o"]

    Note:
        1. 1 <= A.length <= 100
        2. 1 <= A[i].length <= 100
        3. A[i][j] is a lowercase letter
"""
inp= ["bella", "label", "roller"]

class Solution:
    def commonChars(self, A):
        hashCheck = {}
        result = []
        chars = set(A[0])
        for char in chars:
            hashCheck[char] = A[0].count(char)
        for word in A[1:]:
            for key in hashCheck.keys():
                if key not in word:
                    hashCheck[key] = 0
                else:
                    hashCheck[key] = min(hashCheck[key], word.count(key))
        for key, value in hashCheck.items():
            result.extend([key] * value)
        return result

print(Solution().commonChars(inp))
