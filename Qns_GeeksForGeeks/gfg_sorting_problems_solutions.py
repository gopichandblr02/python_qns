# sorting_problems_solutions.py
# Python solutions for all problems from
# "Sorting Coding Problems for Interviews" (GeeksforGeeks)
# https://www.geeksforgeeks.org/top-sorting-interview-questions-and-problems/ :contentReference[oaicite:2]{index=2}

from collections import Counter, defaultdict, deque
import heapq
import bisect
from functools import cmp_to_key

# -------------------------------
# EASY PROBLEMS
# -------------------------------

def max_perimeter_triangle(arr):
    arr.sort(reverse=True)
    for i in range(len(arr)-2):
        if arr[i] < arr[i+1] + arr[i+2]:
            return arr[i] + arr[i+1] + arr[i+2]
    return 0


def maximize_sum_after_k_negations(nums, k):
    nums.sort()
    for i in range(len(nums)):
        if k > 0 and nums[i] < 0:
            nums[i] = -nums[i]
            k -= 1
    return sum(nums) if k % 2 == 0 else sum(nums) - 2 * min(nums)


def sum_min_abs_diff(arr):
    arr.sort()
    return sum(abs(arr[i] - arr[i+1]) for i in range(len(arr)-1))


def sort_in_waveform(arr):
    arr.sort()
    for i in range(0, len(arr)-1, 2):
        arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr


def chocolate_distribution(arr, m):
    arr.sort()
    if m > len(arr):
        return -1
    return min(arr[i+m-1] - arr[i] for i in range(len(arr)-m+1))


def pair_with_given_difference(arr, k):
    s = set(arr)
    return sum(1 for x in arr if x + k in s)

# -------------------------------
# HARD PROBLEMS
# -------------------------------

def merge_sorted_arrays_inplace(a, b):
    import math
    n = len(a)
    m = len(b)
    gap = math.ceil((n + m) / 2)

    def next_gap(g):
        return 0 if g <= 1 else math.ceil(g / 2)

    while gap > 0:
        i = 0
        while i + gap < n:
            if a[i] > a[i+gap]:
                a[i], a[i+gap] = a[i+gap], a[i]
            i += 1

        j = gap - n if gap > n else 0
        while i < n and j < m:
            if a[i] > b[j]:
                a[i], b[j] = b[j], a[i]
            i += 1
            j += 1

        if j < m:
            k = j
            while k + gap < m:
                if b[k] > b[k + gap]:
                    b[k], b[k + gap] = b[k + gap], b[k]
                k += 1

        gap = next_gap(gap)


def count_smaller_on_right(nums):
    res = []
    sorted_list = []
    for x in reversed(nums):
        idx = bisect.bisect_left(sorted_list, x)
        res.append(idx)
        sorted_list.insert(idx, x)
    return res[::-1]


def smallest_non_representable_subset_sum(arr):
    arr.sort()
    res = 1
    for x in arr:
        if x > res:
            break
        res += x
    return res


def count_subarrays_with_median_at_least_x(nums, X):
    for i in range(len(nums)):
        nums[i] = 1 if nums[i] >= X else -1
    prefix = 0
    result = 0
    count = defaultdict(int)
    count[0] = 1
    for val in nums:
        prefix += val
        for k in range(prefix):
            result += count[k]
        count[prefix] += 1
    return result


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def merge_k_sorted_lists(lists):
    heap = []
    for l in lists:
        while l:
            heapq.heappush(heap, l.val)
            l = l.next
    dummy = ListNode(0)
    curr = dummy
    while heap:
        curr.next = ListNode(heapq.heappop(heap))
        curr = curr.next
    return dummy.next


def smallest_difference_triplet(a, b, c):
    i = j = k = 0
    res = float('inf')
    while i < len(a) and j < len(b) and k < len(c):
        maximum = max(a[i], b[j], c[k])
        minimum = min(a[i], b[j], c[k])
        res = min(res, maximum - minimum)
        if minimum == a[i]:
            i += 1
        elif minimum == b[j]:
            j += 1
        else:
            k += 1
    return res


def linear_time_sort_n_to_n2(arr):
    from math import sqrt
    n = int(sqrt(len(arr)))
    buckets = [[] for _ in range(n)]
    for x in arr:
        idx = x // n
        buckets[idx].append(x)
    arr.clear()
    for bucket in buckets:
        arr.extend(sorted(bucket))
    return arr


def diagonal_sort(matrix):
    diagonals = defaultdict(list)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            diagonals[i - j].append(matrix[i][j])

    for key in diagonals:
        diagonals[key].sort(reverse=True)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = diagonals[i - j].pop()
    return matrix


def print_tree_levels_sorted(root):
    q = deque([root])
    while q:
        level_vals = []
        for _ in range(len(q)):
            node = q.popleft()
            level_vals.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        print(sorted(level_vals))

# -------------------------------
# UTILITIES
# -------------------------------

def largest_number(nums):
    def compare(a, b):
        if a + b < b + a:
            return 1
        else:
            return -1
    as_str = list(map(str, nums))
    as_str.sort(key=cmp_to_key(compare))
    return str(int("".join(as_str))) if as_str else ""


def merge_overlapping_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged


def k_most_occurring(arr, k):
    freq = Counter(arr)
    return [x for x, _ in freq.most_common(k)]


def sort_0_1_2(arr):
    low = mid = 0
    high = len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr


def kth_smallest(arr, k):
    return heapq.nsmallest(k, arr)[-1]


def kth_largest(arr, k):
    return heapq.nlargest(k, arr)[-1]


def inversion_count(arr):
    def merge_count(a):
        if len(a) < 2:
            return a, 0
        mid = len(a) // 2
        left, inv_l = merge_count(a[:mid])
        right, inv_r = merge_count(a[mid:])
        merged, inv = [], inv_l + inv_r
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                inv += (len(left) - i)
                j += 1
        return merged + left[i:] + right[j:], inv

    _, total_inv = merge_count(arr)
    return total_inv


def min_platforms(arrival, departure):
    arrival.sort()
    departure.sort()
    plat = result = 0
    i = j = 0
    while i < len(arrival):
        if arrival[i] <= departure[j]:
            plat += 1
            result = max(result, plat)
            i += 1
        else:
            plat -= 1
            j += 1
    return result


def max_meetings(start, end):
    meetings = sorted(zip(end, start))
    result = []
    last_end = -1
    for e, s in meetings:
        if s > last_end:
            result.append((s, e))
            last_end = e
    return result


def case_specific_string_sort(s):
    lowers = sorted([c for c in s if c.islower()])
    uppers = sorted([c for c in s if c.isupper()])
    res = []
    li = ui = 0
    for char in s:
        if char.islower():
            res.append(lowers[li]); li += 1
        else:
            res.append(uppers[ui]); ui += 1
    return "".join(res)


def sort_by_frequency(arr):
    freq = Counter(arr)
    return sorted(arr, key=lambda x: (-freq[x], x))


def min_ops_make_distinct(arr):
    arr.sort()
    moves = 0
    for i in range(1, len(arr)):
        if arr[i] <= arr[i-1]:
            new_val = arr[i-1] + 1
            moves += (new_val - arr[i])
            arr[i] = new_val
    return moves

# End of sorting_problems_solutions.py
