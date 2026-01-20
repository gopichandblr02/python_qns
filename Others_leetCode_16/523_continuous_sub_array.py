def checkSubarraySum(nums, k):
    remainder_map={0:-1}
    running_sum=0

    for i,num in enumerate(nums):
        running_sum+=num
        if k!=0:
            running_sum%=k
        if running_sum in remainder_map:
            if i-remainder_map[running_sum]>=2:
                return True
        else:
            remainder_map[running_sum]=i
    return False

nums = [23, 2, 4, 6, 7]
k = 6

print("output value: ", checkSubarraySum(nums,k))


"""
nums = [23, 2, 4, 6, 7], k = 6

prefixSum % 6:
23 % 6 = 5   → store (5:0)
25 % 6 = 1   → store (1:1)
29 % 6 = 5   → seen before at index 0
current index = 2 → length = 2 → ✅ true

"""