# two_pointers_solutions.py
# Solutions for "Top Problems on Two Pointers Technique for Interviews"
# Source: https://www.geeksforgeeks.org/dsa/top-problems-on-two-pointers-technique-for-interviews/ :contentReference[oaicite:1]{index=1}

from typing import List

# ---------------------- EASY PROBLEMS ----------------------

# 1) Remove Occurrences: Remove all occurrences of val from a list
def remove_occurrences(nums: List[int], val: int) -> List[int]:
    return [x for x in nums if x != val]

# 2) Move Zeros To End
def move_zeros_to_end(nums: List[int]) -> None:
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1

# 3) Unique Elements in Sorted Array
def unique_in_sorted(nums: List[int]) -> List[int]:
    if not nums:
        return nums
    slow = 1
    for fast in range(1, len(nums)):
        if nums[fast] != nums[fast - 1]:
            nums[slow] = nums[fast]
            slow += 1
    return nums[:slow]

# 4) Reverse string preserving space positions
def reverse_preserve_spaces(s: str) -> str:
    arr = list(s)
    left, right = 0, len(arr) - 1
    while left < right:
        if arr[left] == " ":
            left += 1
        elif arr[right] == " ":
            right -= 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    return "".join(arr)

# 5) Sort an array of 0s, 1s and 2s (Dutch National Flag Problem)
def sort_012(nums: List[int]) -> None:
    low, mid, high = 0, 0, len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

# 6) Two Sum (Sorted)
def two_sum_sorted(nums: List[int], target: int) -> bool:
    left, right = 0, len(nums) - 1
    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            return True
        if s < target:
            left += 1
        else:
            right -= 1
    return False

# 7) Pair Sum in a Sorted and Rotated Array
def pair_sum_sorted_rotated(nums: List[int], target: int) -> bool:
    n = len(nums)
    # find pivot
    for i in range(n):
        if nums[i] > nums[(i + 1) % n]:
            break
    left = (i + 1) % n
    right = i
    while left != right:
        s = nums[left] + nums[right]
        if s == target:
            return True
        if s < target:
            left = (left + 1) % n
        else:
            right = (right - 1 + n) % n
    return False

# 8) Closest Pair Sum
def closest_pair_sum(nums: List[int], target: int) -> int:
    nums.sort()
    left, right = 0, len(nums) - 1
    closest = float("inf")
    result = 0
    while left < right:
        current_sum = nums[left] + nums[right]
        if abs(target - current_sum) < abs(target - closest):
            closest = current_sum
            result = current_sum
        if current_sum < target:
            left += 1
        else:
            right -= 1
    return result

# 9) Closest pair from two sorted arrays
def closest_pair_two_arrays(a: List[int], b: List[int], x: int) -> int:
    i, j = 0, len(b) - 1
    closest = float("inf")
    while i < len(a) and j >= 0:
        s = a[i] + b[j]
        if abs(x - s) < abs(x - closest):
            closest = s
        if s > x:
            j -= 1
        else:
            i += 1
    return closest

# 10) Smallest Subarray > Sum
def smallest_subarray_with_sum(nums: List[int], target: int) -> int:
    left = 0
    s = 0
    min_len = float("inf")
    for right, val in enumerate(nums):
        s += val
        while s > target:
            min_len = min(min_len, right - left + 1)
            s -= nums[left]
            left += 1
    return min_len if min_len != float("inf") else 0

# 11) Dominant Pairs (count pairs with i < j and nums[i] >= nums[j] * 5)
def dominant_pairs(nums: List[int]) -> int:
    count = 0
    left = 0
    right = len(nums) - 1
    while left < right:
        if nums[left] >= nums[right] * 5:
            count += 1
            right -= 1
        else:
            left += 1
    return count

# 12) Sentence Palindrome
def is_sentence_palindrome(s: str) -> bool:
    filtered = [c.lower() for c in s if c.isalnum()]
    return filtered == filtered[::-1]

# 13) Intersection of Arrays with Distinct
def intersection_distinct(a: List[int], b: List[int]) -> List[int]:
    return list(set(a).intersection(set(b)))

# ---------------------- MEDIUM PROBLEMS ----------------------

# 14) Count pairs with absolute difference equal to k
def count_pairs_diff_k(nums: List[int], k: int) -> int:
    nums.sort()
    left, right = 0, 1
    count = 0
    while right < len(nums):
        diff = nums[right] - nums[left]
        if diff == k:
            count += 1
            right += 1
            left += 1
        elif diff < k:
            right += 1
        else:
            left += 1
            if left == right:
                right += 1
    return count

# 15) Triplet Sum in Array
def triplet_sum(nums: List[int], target: int) -> bool:
    nums.sort()
    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s == target:
                return True
            if s < target:
                left += 1
            else:
                right -= 1
    return False

# 16) Sum of Two Equals Third
def sum_of_two_equals_third(nums: List[int]) -> bool:
    nums.sort()
    for i in range(len(nums)):
        target = nums[i]
        l, r = 0, len(nums) - 1
        while l < r:
            if l == i:
                l += 1
                continue
            if r == i:
                r -= 1
                continue
            s = nums[l] + nums[r]
            if s == target:
                return True
            if s < target:
                l += 1
            else:
                r -= 1
    return False

# 17) K-th element of two Arrays
def kth_element_two_arrays(a: List[int], b: List[int], k: int) -> int:
    i = j = 0
    merged = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1
        if len(merged) == k:
            return merged[-1]
    while i < len(a):
        merged.append(a[i])
        i += 1
        if len(merged) == k:
            return merged[-1]
    while j < len(b):
        merged.append(b[j])
        j += 1
        if len(merged) == k:
            return merged[-1]
    return -1

# 18) Union of 2 Sorted with Duplicates
def union_sorted(a: List[int], b: List[int]) -> List[int]:
    i = j = 0
    result = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        elif a[i] > b[j]:
            result.append(b[j])
            j += 1
        else:
            result.append(a[i])
            i += 1
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result

# 19) Subarrays with Max in Range
def subarrays_with_max_in_range(nums: List[int], left: int, right: int) -> int:
    count = 0
    start = -1
    prev = -1
    for i, v in enumerate(nums):
        if left <= v <= right:
            prev = i
        if v > right:
            start = i
        count += max(0, prev - start)
    return count

# 20) Longest Substring with K Unique
def longest_substring_k_unique(s: str, k: int) -> int:
    from collections import defaultdict
    left = 0
    freq = defaultdict(int)
    max_len = 0
    for right, ch in enumerate(s):
        freq[ch] += 1
        while len(freq) > k:
            freq[s[left]] -= 1
            if freq[s[left]] == 0:
                del freq[s[left]]
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len

# 21) Remove and Reverse
def remove_and_reverse(s: str, remove: str) -> str:
    filtered = [c for c in s if c != remove]
    return "".join(filtered[::-1])

# 22) The Celebrity Problem
def find_celebrity(M: List[List[int]]) -> int:
    n = len(M)
    a = 0
    b = n - 1
    while a < b:
        if M[a][b] == 1:
            a += 1
        else:
            b -= 1
    for i in range(n):
        if i != a and (M[a][i] == 1 or M[i][a] == 0):
            return -1
    return a

# ---------------------- HARD PROBLEMS ----------------------

# 23) Trapping Rain Water
def trapping_rain_water(height: List[int]) -> int:
    left, right = 0, len(height) - 1
    left_max = right_max = 0
    water = 0
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1
    return water

# 24) 4 Sum - Check for Quadruple
def four_sum_exists(nums: List[int], target: int) -> bool:
    nums.sort()
    n = len(nums)
    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            left = j + 1
            right = n - 1
            while left < right:
                s = nums[i] + nums[j] + nums[left] + nums[right]
                if s == target:
                    return True
                if s < target:
                    left += 1
                else:
                    right -= 1
    return False

# 25) 4 Sum – All Distinct Quadruplets
def four_sum_all(nums: List[int], target: int) -> List[List[int]]:
    nums.sort()
    n = len(nums)
    results = []
    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i + 1, n - 2):
            if j > i+1 and nums[j] == nums[j-1]:
                continue
            left = j + 1
            right = n - 1
            while left < right:
                s = nums[i]+nums[j]+nums[left]+nums[right]
                if s == target:
                    results.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif s < target:
                    left += 1
                else:
                    right -= 1
    return results
