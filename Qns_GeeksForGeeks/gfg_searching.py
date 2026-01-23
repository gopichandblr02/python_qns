# top_searching_problems_optimized.py
# Single-file collection of optimized solutions for Top ~50 Searching / Binary Search style problems
# All solutions use Python 3 and aim for clarity + optimal time complexity
# Most are O(log n) using binary search variants

from typing import List, Optional


# =============================================================================
# 1. Linear Search (baseline – O(n))
# =============================================================================
def linear_search(arr: List[int], target: int) -> int:
    """Return index of target or -1"""
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1


# =============================================================================
# 2. Binary Search – Standard (sorted array) – O(log n)
# =============================================================================
def binary_search(arr: List[int], target: int) -> int:
    """Assumes arr is sorted ascending. Returns index or -1"""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# =============================================================================
# 3. First Occurrence / Lower Bound (sorted array, duplicates allowed)
# =============================================================================
def first_occurrence(arr: List[int], target: int) -> int:
    """Leftmost index where target appears or -1"""
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1          # continue searching left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result


# =============================================================================
# 4. Last Occurrence / Upper Bound – 1
# =============================================================================
def last_occurrence(arr: List[int], target: int) -> int:
    """Rightmost index where target appears or -1"""
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            result = mid
            left = mid + 1           # continue searching right
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result


# =============================================================================
# 5. Count occurrences using first & last
# =============================================================================
def count_occurrences(arr: List[int], target: int) -> int:
    first = first_occurrence(arr, target)
    if first == -1:
        return 0
    last = last_occurrence(arr, target)
    return last - first + 1


# =============================================================================
# 6. Search in Rotated Sorted Array (no duplicates) – LeetCode 33
# =============================================================================
def search_rotated_sorted(arr: List[int], target: int) -> int:
    """O(log n) – find target in rotated sorted array (unique elements)"""
    if not arr:
        return -1
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        # Left half is sorted
        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


# =============================================================================
# 7. Search in Rotated Sorted Array with Duplicates – LeetCode 81
# =============================================================================
def search_rotated_with_duplicates(arr: List[int], target: int) -> bool:
    """O(log n) average, O(n) worst case due to duplicates"""
    if not arr:
        return False
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return True
        if arr[left] == arr[mid] == arr[right]:
            left += 1
            right -= 1
            continue
        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    return False


# =============================================================================
# 8. Find Minimum in Rotated Sorted Array – LeetCode 153
# =============================================================================
def find_min_rotated(arr: List[int]) -> int:
    """O(log n) – returns smallest element"""
    left, right = 0, len(arr) - 1
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] > arr[right]:
            left = mid + 1
        else:
            right = mid
    return arr[left]


# =============================================================================
# 9. Search a 2D Matrix – LeetCode 74
# =============================================================================
def search_matrix(matrix: List[List[int]], target: int) -> bool:
    """Treat 2D matrix as 1D sorted array – O(log(m*n))"""
    if not matrix or not matrix[0]:
        return False
    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1
    while left <= right:
        mid = left + (right - left) // 2
        row, col = divmod(mid, cols)
        val = matrix[row][col]
        if val == target:
            return True
        if val < target:
            left = mid + 1
        else:
            right = mid - 1
    return False


# =============================================================================
# 10. Find Peak Element – LeetCode 162
# =============================================================================
def find_peak_element(nums: List[int]) -> int:
    """O(log n) – any peak index is fine (adjacent elements differ)"""
    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left


# =============================================================================
# 11. Exponential Search (good for unbounded / very large sorted arrays)
# =============================================================================
def exponential_search(arr: List[int], target: int) -> int:
    """O(log i) where i is position – useful when array is very large"""
    if arr[0] == target:
        return 0
    i = 1
    n = len(arr)
    while i < n and arr[i] <= target:
        i *= 2
    # Now do binary search in arr[i//2 : min(i, n)]
    left = i // 2
    right = min(i, n - 1)
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# =============================================================================
# 12. Find Floor / Greatest element <= target
# =============================================================================
def find_floor(arr: List[int], target: int) -> int:
    """Index of greatest element <= target, or -1"""
    left, right = 0, len(arr) - 1
    res = -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            res = mid
            left = mid + 1
        else:
            right = mid - 1
    return res


# =============================================================================
# 13. Find Ceil / Smallest element >= target
# =============================================================================
def find_ceil(arr: List[int], target: int) -> int:
    """Index of smallest element >= target, or -1"""
    left, right = 0, len(arr) - 1
    res = -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] > target:
            res = mid
            right = mid - 1
        else:
            left = mid + 1
    return res


# =============================================================================
# 14. Search in Bitonic Array (increases then decreases)
# =============================================================================
def search_bitonic(arr: List[int], target: int) -> int:
    """O(log n) – find peak first, then binary search both sides"""
    if not arr:
        return -1
    # Find peak index
    left, right = 0, len(arr) - 1
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid
    peak = left

    # Search left side (ascending)
    l, r = 0, peak
    while l <= r:
        m = l + (r - l) // 2
        if arr[m] == target:
            return m
        if arr[m] < target:
            l = m + 1
        else:
            r = m - 1

    # Search right side (descending)
    l, r = peak + 1, len(arr) - 1
    while l <= r:
        m = l + (r - l) // 2
        if arr[m] == target:
            return m
        if arr[m] > target:
            l = m + 1
        else:
            r = m - 1
    return -1


# =============================================================================
# Utility / Test harness
# =============================================================================
def run_tests():
    tests = [
        # (function, args, expected)
        (binary_search, ([1,3,5,7,9], 5), 2),
        (first_occurrence, ([1,2,2,2,3,4], 2), 1),
        (last_occurrence, ([1,2,2,2,3,4], 2), 3),
        (search_rotated_sorted, ([4,5,6,7,0,1,2], 0), 4),
        (find_min_rotated, ([4,5,6,7,0,1,2]), 0),
        (search_matrix, ([[1,3,5],[6,7,12],[15,18,20]], 7), True),
        (find_peak_element, ([1,2,3,1]), 2),
    ]

    for func, (args, expected) in tests:
        result = func(*args) if isinstance(args, tuple) else func(args)
        print(f"{func.__name__}{args} → {result}  (expected {expected})")


if __name__ == "__main__":
    print("Running sample tests...\n")
    run_tests()
    print("\nThis file contains optimized searching solutions commonly asked in interviews.")
    print("Most use binary search or its variants → O(log n) time.")