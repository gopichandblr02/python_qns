def binary_search(nums,target):
    start=0
    end=len(nums)-1
    while start <= end:
        mid = start + end // 2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            start=mid+1
        else:
            end=mid-1
    return -1

nums = [1, 3, 5, 7, 9, 12]
print(binary_search(nums, 7))   # 3
print(binary_search(nums, 4))   # -1