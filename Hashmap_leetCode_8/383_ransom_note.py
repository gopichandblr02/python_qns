"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
"""


class Solution:
    def canConstruct(self, ransomNote, magazine):
        freq = {}
        # Count characters in magazine
        for ch in magazine:
            freq[ch] = freq.get(ch, 0) + 1

        # Check ransom note
        for ch in ransomNote:
            if ch not in freq or freq[ch] == 0:
                return False
            freq[ch] -= 1

        return True

    def canConstruct_FAANG(ransomNote, magazine):
        count = [0] * 26

        # What does ord(ch) - ord('a') do?
        # ord(ch) → ASCII value of character
        # 'a' = 97, 'b' = 98, ..., 'z' = 122

        # ch = 'c'
        # ord('c') = 99
        # 99 - 97 = 2  → index
        # for 'c'

        for ch in magazine:
            count[ord(ch) - ord('a')] += 1

        for ch in ransomNote:
            idx = ord(ch) - ord('a')
            if count[idx] == 0:
                return False
            count[idx] -= 1

        return True


ransomNote = "aa"
magazine = "aab"
print(Solution().canConstruct(ransomNote,magazine))

print(Solution().canConstruct_FAANG(ransomNote,magazine))