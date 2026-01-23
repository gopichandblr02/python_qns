"""
Top 50 Array Coding Problems – GeeksforGeeks
Easy + Medium + Hard (Optimized Python Solutions)

Each function corresponds to a classic interview problem.
Time & space complexities are optimal / standard accepted solutions.
"""

# -------------------- EASY --------------------

def largest_element(arr):
    return max(arr)

def second_largest(arr):
    first = second = float('-inf')
    for x in arr:
        if x > first:
            first, second = x, first
        elif first > x > second:
            second = x
    return second

def reverse_array(arr):
    return arr[::-1]

def rotate_array(arr, k):
    k %= len(arr)
    return arr[k:] + arr[:k]

def is_sorted(arr):
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))

########################################################
######################## all ###########################
########################################################

# All values are truthy (non-zero or non-empty)
list1 = [1, 3, 4, 5]
print(all(list1))  # Output: True

# Contains a falsy value (0)
list2 = [1, 3, 4, 0]
print(all(list2))  # Output: False

# Empty iterable
list3 = []
print(all(list3))  # Output: True

# With a dictionary (checks keys only)
dict1 = {1: 'True', 2: 'True'}
print(all(dict1)) # Output: True (keys 1 and 2 are truthy)

dict2 = {0: 'False', 1: 'False'}
print(all(dict2)) # Output: False (key 0 is falsy)
####

def remove_duplicates_sorted(arr):
    j = 0
    for i in range(1, len(arr)):
        if arr[i] != arr[j]:
            j += 1
            arr[j] = arr[i]
    return j + 1

def move_zeros(arr):
    j = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[j], arr[i] = arr[i], arr[j]
            j += 1
    return arr

def missing_number(arr, n):
    return n*(n+1)//2 - sum(arr)

def union_arrays(a, b):
    return sorted(set(a) | set(b))

def intersection_arrays(a, b):
    return sorted(set(a) & set(b))


# -------------------- MEDIUM --------------------

def kadane(arr):
    curr = best = arr[0]
    for x in arr[1:]:
        curr = max(x, curr + x)
        best = max(best, curr)
    return best

def leaders(arr):
    max_from_right = float('-inf')
    res = []
    for x in reversed(arr):
        if x > max_from_right:
            res.append(x)
            max_from_right = x
    return res[::-1]

def equilibrium_index(arr):
    total = sum(arr)
    left = 0
    for i, x in enumerate(arr):
        total -= x
        if left == total:
            return i
        left += x
    return -1

def majority_element(arr):
    count = 0
    candidate = None
    for x in arr:
        if count == 0:
            candidate = x
        count += 1 if x == candidate else -1
    return candidate

def rearrange_alternate(arr):
    pos = [x for x in arr if x >= 0]
    neg = [x for x in arr if x < 0]
    res = []
    i = j = 0
    while i < len(pos) and j < len(neg):
        res.append(pos[i]); res.append(neg[j])
        i += 1; j += 1
    res.extend(pos[i:])
    res.extend(neg[j:])
    return res

def stock_buy_sell(prices):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]
    return profit

def count_pairs_with_sum(arr, k):
    from collections import Counter
    freq = Counter(arr)
    count = 0
    for x in freq:
        if k-x in freq:
            count += freq[x] * freq[k-x]
    return count//2

def merge_intervals(intervals):
    intervals.sort()
    res = [intervals[0]]
    for s, e in intervals[1:]:
        if s <= res[-1][1]:
            res[-1][1] = max(res[-1][1], e)
        else:
            res.append([s, e])
    return res

def subarray_with_sum(arr, target):
    curr = start = 0
    for end, x in enumerate(arr):
        curr += x
        while curr > target:
            curr -= arr[start]
            start += 1
        if curr == target:
            return (start, end)
    return None


# -------------------- HARD --------------------

def trap_rain_water(height):
    l, r = 0, len(height) - 1
    left_max = right_max = 0
    water = 0
    while l < r:
        if height[l] < height[r]:
            left_max = max(left_max, height[l])
            water += left_max - height[l]
            l += 1
        else:
            right_max = max(right_max, height[r])
            water += right_max - height[r]
            r -= 1
    return water

def max_circular_subarray_sum(arr):
    def kadane(a):
        curr = best = a[0]
        for x in a[1:]:
            curr = max(x, curr + x)
            best = max(best, curr)
        return best
    total = sum(arr)
    return max(kadane(arr), total + kadane([-x for x in arr]))

def smallest_missing_positive(arr):
    n = len(arr)
    for i in range(n):
        while 1 <= arr[i] <= n and arr[arr[i]-1] != arr[i]:
            j = arr[i] - 1
            arr[i], arr[j] = arr[j], arr[i]
    for i in range(n):
        if arr[i] != i + 1:
            return i + 1
    return n + 1

def can_jump(nums):
    reach = 0
    for i, x in enumerate(nums):
        if i > reach:
            return False
        reach = max(reach, i + x)
    return True

def smallest_non_representable(arr):
    res = 1
    for x in sorted(arr):
        if x > res:
            break
        res += x
    return res

def max_sum_rotation(arr):
    n = len(arr)
    arr_sum = sum(arr)
    curr_val = sum(i*arr[i] for i in range(n))
    res = curr_val
    for i in range(1, n):
        curr_val += arr_sum - n*arr[n-i]
        res = max(res, curr_val)
    return res

def count_subarrays_k_distinct(arr, k):
    from collections import defaultdict
    def at_most(k):
        freq = defaultdict(int)
        left = res = 0
        for right, x in enumerate(arr):
            if freq[x] == 0:
                k -= 1
            freq[x] += 1
            while k < 0:
                freq[arr[left]] -= 1
                if freq[arr[left]] == 0:
                    k += 1
                left += 1
            res += right - left + 1
        return res
    return at_most(k) - at_most(k-1)