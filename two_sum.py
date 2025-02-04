# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# 2 5 4.   target 6
# 0 1 2
# {4:0,1:1,2:2}

def sum_two(nums, target):
    seen = {}
    for i,num in enumerate(nums):
        rem = target-num
        if rem in seen:
            return [seen[rem],i]
        else:
            seen[num]=i
    return []

print(sum_two([2,5,4],6))