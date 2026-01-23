# sliding_window_problems_solutions.py
# Python solutions for sliding window interview problems
# Source: GeeksforGeeks “Top Problems on Sliding Window Technique for Interviews” :contentReference[oaicite:1]{index=1}

from collections import deque, Counter, defaultdict
import math

# 1) Maximum sum of a subarray of size k
def max_sum_subarray_k(arr, k):
    if not arr or k <= 0 or k > len(arr):
        return 0
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum

# 2) Smallest window containing 0, 1 and 2
def smallest_window_012(arr):
    required = {'0','1','2'}
    left = 0
    found = Counter()
    min_len = math.inf
    count = 0
    for right, v in enumerate(arr):
        found[str(v)] += 1
        if found[str(v)] == 1:
            count += 1
        while count == 3:
            min_len = min(min_len, right - left + 1)
            found[str(arr[left])] -= 1
            if found[str(arr[left])] == 0:
                count -= 1
            left += 1
    return min_len if min_len != math.inf else 0

# 3) Check if Permutation of Pattern is Substring
def check_permutation_substring(s, p):
    len_p, len_s = len(p), len(s)
    if len_p > len_s:
        return False
    freq_p = Counter(p)
    window = Counter()
    for i in range(len_s):
        window[s[i]] += 1
        if i >= len_p:
            left_char = s[i - len_p]
            if window[left_char] == 1:
                del window[left_char]
            else:
                window[left_char] -= 1
        if window == freq_p:
            return True
    return False

# 4) Count Strictly Increasing Subarrays
def count_increasing_subarrays(arr):
    count = 1
    total = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            count += 1
        else:
            total += count*(count+1)//2
            count = 1
    total += count*(count+1)//2
    return total

# 5) Remove Consecutive Characters (reduce same adjacents)
def remove_consecutive_chars(s):
    result = []
    for ch in s:
        if not result or result[-1] != ch:
            result.append(ch)
    return "".join(result)

# 6) Maximum sum subarray <= x
def max_sum_subarray_leq_x(arr, x):
    left = 0
    window_sum = 0
    max_sum = -math.inf
    for right in range(len(arr)):
        window_sum += arr[right]
        while window_sum > x and left <= right:
            window_sum -= arr[left]
            left += 1
        max_sum = max(max_sum, window_sum)
    return max_sum

# 7) Longest substring with distinct characters
def longest_distinct_substring(s):
    last_seen = {}
    start = 0
    max_len = 0
    for i, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= start:
            start = last_seen[ch] + 1
        last_seen[ch] = i
        max_len = max(max_len, i - start + 1)
    return max_len

# 8) Substrings with K distinct
def substrings_k_distinct(s, k):
    count = 0
    freq = {}
    left = 0
    for right in range(len(s)):
        freq[s[right]] = freq.get(s[right], 0) + 1
        while len(freq) > k and left <= right:
            freq[s[left]] -= 1
            if freq[s[left]] == 0:
                del freq[s[left]]
            left += 1
        if len(freq) == k:
            count += right - left + 1
    return count

# 9) Maximum Fruits in Two Baskets (Longest subarray with at most 2 distinct)
def max_fruits_two_baskets(arr):
    return longest_subarray_k_distinct(arr, 2)

def longest_subarray_k_distinct(arr, k):
    freq = {}
    left = 0
    max_len = 0
    for right in range(len(arr)):
        freq[arr[right]] = freq.get(arr[right], 0) + 1
        while len(freq) > k:
            freq[arr[left]] -= 1
            if freq[arr[left]] == 0:
                del freq[arr[left]]
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len

# 10) Substrings length k with k‑1 distinct
def substrings_k_kminus1_distinct(s, k):
    return [s[i:i+k] for i in range(len(s)-k+1)
            if len(set(s[i:i+k])) == k-1]

# 11) Minimum Removals for Target Sum (smallest subarray removal so sum <= target)
def min_removals_target_sum(arr, target):
    left = 0
    window_sum = 0
    max_len = 0
    total = sum(arr)
    needed = total - target
    if needed <= 0:
        return 0
    for right in range(len(arr)):
        window_sum += arr[right]
        while window_sum >= needed:
            max_len = max(max_len, right-left+1)
            window_sum -= arr[left]
            left += 1
    return max_len

# 12) Longest Repeating Character Replacement
def longest_repeating_char_replace(s, k):
    freq = {}
    left = 0
    max_count = 0
    result = 0
    for right in range(len(s)):
        freq[s[right]] = freq.get(s[right], 0) + 1
        max_count = max(max_count, freq[s[right]])
        while (right - left + 1) - max_count > k:
            freq[s[left]] -= 1
            left += 1
        result = max(result, right - left + 1)
    return result

# 13) Binary subarray with sum (count subarrays equal to sum S)
def count_binary_subarray_sum(arr, S):
    seen = {0: 1}
    cum_sum = 0
    count = 0
    for num in arr:
        cum_sum += num
        if cum_sum-S in seen:
            count += seen[cum_sum-S]
        seen[cum_sum] = seen.get(cum_sum, 0) + 1
    return count

# 14) Subarrays Product Less than K
def subarrays_product_less_than_k(arr, k):
    if k <= 1:
        return 0
    prod = 1
    left = 0
    result = 0
    for right in range(len(arr)):
        prod *= arr[right]
        while prod >= k:
            prod /= arr[left]
            left += 1
        result += right - left + 1
    return result

# 15) Count Occurrences of Anagrams
def count_anagram_occurrences(s, p):
    len_p = len(p)
    freq_p = Counter(p)
    window = Counter()
    count = 0
    for i in range(len(s)):
        window[s[i]] += 1
        if i >= len_p:
            left = s[i - len_p]
            window[left] -= 1
            if window[left] == 0:
                del window[left]
        if window == freq_p:
            count += 1
    return count

# 16) Largest sum subarray of size at least k
def largest_sum_subarray_at_least_k(arr, k):
    # Kadane + sliding window
    n = len(arr)
    max_sum = -math.inf
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, n):
        window_sum += arr[i]
        max_sum = max(max_sum, window_sum)
    # also consider subarrays > k by extending with Kadane
    curr_max = arr[0]
    for i in range(1,n):
        curr_max = max(arr[i], curr_max+arr[i])
        max_sum = max(max_sum, curr_max)
    return max_sum

# 17) Count Distinct Elements In Every Window of Size K
def distinct_in_every_window(arr, k):
    freq = Counter(arr[:k])
    result = [len(freq)]
    for i in range(k, len(arr)):
        freq[arr[i]] += 1
        freq[arr[i-k]] -= 1
        if freq[arr[i-k]] == 0:
            del freq[arr[i-k]]
        result.append(len(freq))
    return result

# 18) Subarray with given sum (positive integers)
def subarray_with_given_sum(arr, target):
    left = 0
    curr_sum = 0
    for right in range(len(arr)):
        curr_sum += arr[right]
        while curr_sum > target and left <= right:
            curr_sum -= arr[left]
            left += 1
        if curr_sum == target:
            return (left, right)
    return (-1, -1)

# 19) First negative integer in every window of size k
def first_negative_in_windows(arr, k):
    result = []
    dq = deque()
    for i in range(len(arr)):
        if arr[i] < 0:
            dq.append(i)
        if i >= k-1:
            while dq and dq[0] < i-k+1:
                dq.popleft()
            result.append(arr[dq[0]] if dq else 0)
    return result

# 20) Longest Subarray With Sum K
def longest_subarray_with_sum_k(arr, K):
    sum_index = {0: -1}
    cum_sum = 0
    max_len = 0
    for i, num in enumerate(arr):
        cum_sum += num
        if cum_sum-K in sum_index:
            max_len = max(max_len, i - sum_index[cum_sum-K])
        if cum_sum not in sum_index:
            sum_index[cum_sum] = i
    return max_len

# 21) Smallest window that contains all characters of string itself
def smallest_window_all_chars(s):
    return smallest_window_substring(s,s)

# 22) Smallest window in a String containing all characters of other String
def smallest_window_substring(s, t):
    need = Counter(t)
    missing = len(t)
    left = start = end = 0
    for right, ch in enumerate(s):
        if need[ch] > 0:
            missing -= 1
        need[ch] -= 1
        while missing == 0:
            if end == 0 or right-left+1 < end-start+1:
                start, end = left, right
            need[s[left]] += 1
            if need[s[left]] > 0:
                missing += 1
            left += 1
    return s[start:end+1] if end>=start else ""

# 23) Equivalent Sub‑Arrays (Count subarrays same in two arrays)
def equivalent_subarrays(arr1, arr2):
    diff_map = defaultdict(int)
    count = 0
    cum1 = cum2 = 0
    for i in range(len(arr1)):
        cum1 += arr1[i]
        cum2 += arr2[i]
        diff_map[cum1-cum2] += 1
        count += diff_map[cum1-cum2] - 1
    return count

# 24) Maximum of minimum for every window size (classic)
def max_of_min_for_every_window(arr):
    n = len(arr)
    left = [-1]*n
    right = [n]*n
    stack=[]
    for i in range(n):
        while stack and arr[stack[-1]]>=arr[i]:
            stack.pop()
        left[i] = stack[-1] if stack else -1
        stack.append(i)
    stack=[]
    for i in range(n-1,-1,-1):
        while stack and arr[stack[-1]]>=arr[i]:
            stack.pop()
        right[i]=stack[-1] if stack else n
        stack.append(i)
    res = [0]*(n+1)
    for i in range(n):
        length = right[i]-left[i]-1
        res[length]=max(res[length],arr[i])
    for i in range(n-1,0,-1):
        res[i]=max(res[i],res[i+1])
    return res[1:]

# 25) Longest Substring with K Uniques
def longest_substring_k_uniques(s, k):
    return longest_subarray_k_distinct(s, k)

# 26) Minimum Window Substring
def minimum_window_substring(s, t):
    return smallest_window_substring(s,t)

# 27) Largest sum subarray with at‑least k numbers
def largest_sum_subarray_min_k(arr, k):
    return largest_sum_subarray_at_least_k(arr, k)
