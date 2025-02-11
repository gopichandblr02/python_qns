def max_subarray_sum(nums):
    """
    Finds the contiguous sublist with the largest sum.

    Args:
        nums: A list of numbers.

    Returns:
        The maximum sum of a contiguous sublist.
    """
    max_so_far = float('-inf')  # Initialize to negative infinity
    current_max = 0
    start_index = 0
    end_index = 0
    j = 0

    for i, num in enumerate(nums):
        current_max += num

        if current_max > max_so_far:
            max_so_far = current_max
            start_index = j
            end_index = i

        if current_max < 0:
            current_max = 0
            j = i + 1

    return max_so_far, start_index, end_index

# Example usage
numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum, start, end = max_subarray_sum(numbers)

print("Maximum sum:", max_sum)
print("Start index:", start)
print("End index:", end)
print("Sublist:", numbers[start:end+1])