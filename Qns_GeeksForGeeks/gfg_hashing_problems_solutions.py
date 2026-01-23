# hashing_problems_solutions.py
# Python solutions for algorithmic problems from
# "Top 20 Hashing Technique based Interview Questions" (GeeksforGeeks)
# Only algorithmic coding problems (1-17)
# https://www.geeksforgeeks.org/top-20-hashing-technique-based-interview-questions/?utm_source=chatgpt.com

from collections import defaultdict, Counter

# -------------------------------
# 1. Subset Check
def is_subset(arr1, arr2):
    set1 = set(arr1)
    return all(x in set1 for x in arr2)

# 2. Union and Intersection of two Linked Lists
def union_intersection(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    union = list(set1 | set2)
    intersection = list(set1 & set2)
    return union, intersection

# 3. A Pair With Given Sum
def has_pair_with_sum(arr, k):
    seen = set()
    for num in arr:
        if k - num in seen:
            return True
        seen.add(num)
    return False

# 4. Two Pair Sum (find all unique pairs with sum = k)
def all_pairs_with_sum(arr, k):
    seen = set()
    pairs = set()
    for num in arr:
        if k - num in seen:
            pairs.add(tuple(sorted((num, k - num))))
        seen.add(num)
    return list(pairs)

# 5. Largest Subarray With 0 Sum
def largest_subarray_zero_sum(arr):
    sum_map = {}
    max_len = 0
    cum_sum = 0
    for i, num in enumerate(arr):
        cum_sum += num
        if cum_sum == 0:
            max_len = i + 1
        if cum_sum in sum_map:
            max_len = max(max_len, i - sum_map[cum_sum])
        else:
            sum_map[cum_sum] = i
    return max_len

# 6. Distinct Elements in Every K-size Window
def distinct_in_windows(arr, k):
    n = len(arr)
    if k > n:
        return []
    freq = Counter(arr[:k])
    result = [len(freq)]
    for i in range(k, n):
        freq[arr[i]] += 1
        freq[arr[i-k]] -= 1
        if freq[arr[i-k]] == 0:
            del freq[arr[i-k]]
        result.append(len(freq))
    return result

# 7. Palindrome Substring Queries
def is_palindrome_substring(s, queries):
    n = len(s)
    prefix = [[0]*26 for _ in range(n+1)]
    for i in range(n):
        prefix[i+1] = prefix[i][:]
        prefix[i+1][ord(s[i])-ord('a')] += 1
    res = []
    for l,r in queries:
        odd_count = sum((prefix[r+1][i]-prefix[l][i])%2 for i in range(26))
        res.append(odd_count <= 1)
    return res

# 8. Missing Elements of a Range
def missing_elements(arr, low, high):
    present = set(arr)
    return [x for x in range(low, high+1) if x not in present]

# 9. All Subarrays With 0 Sum
def all_subarrays_zero_sum(arr):
    sum_map = defaultdict(list)
    cum_sum = 0
    res = []
    for i, num in enumerate(arr):
        cum_sum += num
        if cum_sum == 0:
            res.append((0, i))
        if cum_sum in sum_map:
            for start in sum_map[cum_sum]:
                res.append((start+1, i))
        sum_map[cum_sum].append(i)
    return res

# 10. Symmetric Pairs
def symmetric_pairs(pairs):
    seen = {}
    res = []
    for x,y in pairs:
        if (y in seen) and seen[y]==x:
            res.append((x,y))
        else:
            seen[x]=y
    return res

# 11. Duplicates Within K Distance
def has_duplicate_within_k(arr, k):
    seen = {}
    for i, val in enumerate(arr):
        if val in seen and i - seen[val] <= k:
            return True
        seen[val] = i
    return False

# 12. Find Itinerary From Given Tickets
def find_itinerary(tickets, start):
    graph = defaultdict(list)
    for src,dest in tickets:
        graph[src].append(dest)
    for src in graph:
        graph[src].sort(reverse=True)
    route=[]
    def visit(node):
        while graph[node]:
            visit(graph[node].pop())
        route.append(node)
    visit(start)
    return route[::-1]

# 13. Largest Subarray With Equal Number of 0s and 1s
def largest_subarray_equal_0_1(arr):
    arr = [1 if x==1 else -1 for x in arr]
    sum_map = {}
    cum_sum = 0
    max_len = 0
    for i, num in enumerate(arr):
        cum_sum += num
        if cum_sum == 0:
            max_len = i+1
        if cum_sum in sum_map:
            max_len = max(max_len, i-sum_map[cum_sum])
        else:
            sum_map[cum_sum] = i
    return max_len

# 14. Count Subarrays With XOR
def count_subarrays_with_xor(arr, K):
    xor_map = defaultdict(int)
    res = 0
    cum_xor = 0
    for num in arr:
        cum_xor ^= num
        if cum_xor == K:
            res += 1
        res += xor_map[cum_xor ^ K]
        xor_map[cum_xor] += 1
    return res

# 15. Longest Consecutive Subsequence
def longest_consecutive_subsequence(arr):
    s = set(arr)
    max_len = 0
    for num in arr:
        if num-1 not in s:
            curr = num
            length = 1
            while curr+1 in s:
                curr += 1
                length += 1
            max_len = max(max_len, length)
    return max_len

# 16. Pair Sum Divisible by K
def pair_sum_divisible_by_k(arr, K):
    freq = [0]*K
    count = 0
    for num in arr:
        freq[num%K] += 1
    count += freq[0]*(freq[0]-1)//2
    for i in range(1,(K+1)//2):
        count += freq[i]*freq[K-i]
    if K%2==0:
        count += freq[K//2]*(freq[K//2]-1)//2
    return count

# 17. Smallest Range From K Lists
import heapq
def smallest_range(lists):
    min_heap=[]
    current_max=float('-inf')
    for i,lst in enumerate(lists):
        val=lst[0]
        heapq.heappush(min_heap,(val,i,0))
        current_max=max(current_max,val)
    res=[float('-inf'),float('inf')]
    while True:
        val,row,col=heapq.heappop(min_heap)
        if current_max - val < res[1]-res[0]:
            res=[val,current_max]
        if col+1==len(lists[row]):
            break
        next_val=lists[row][col+1]
        heapq.heappush(min_heap,(next_val,row,col+1))
        current_max=max(current_max,next_val)
    return res

# -------------------------------
# END OF FILE
# -------------------------------
