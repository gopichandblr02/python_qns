def quick_sort(arr):
    arr_len=len(arr)
    if arr_len<=1:
        return arr
    pivot_element = arr[arr_len//2]
    left_arr=[x for x in arr if x<pivot_element]
    middle_element = [x for x in arr if x == pivot_element]
    right_arr=[x for x in arr if x>pivot_element]
    return quick_sort(left_arr)+middle_element+quick_sort(right_arr)

if __name__=="__main__":
    arr = [10,7,8,9,1,5]
    print(quick_sort(arr))

"""
🔥 Quick Sort vs Merge Sort — Which Is Better?
✅ 1. Time Complexity
Algorithm	Best	Average	Worst
Quick Sort	O(n log n)	O(n log n)	O(n²)
Merge Sort	O(n log n)	O(n log n)	O(n log n)

Quick Sort can degrade to O(n²) (e.g., already sorted input + bad pivot).

Merge Sort is always stable O(n log n).

💾 2. Space Complexity
Algorithm	Space
Quick Sort	O(log n) (in-place)
Merge Sort	O(n) (needs extra array)

Merge Sort requires extra space to merge.

Quick Sort usually uses recursion stack only → much more space-efficient.

🚀 3. Practical Performance
Quick Sort:

Usually faster in practice due to better cache locality.

Minimal memory usage.

Used in many standard library sorts (with optimizations).

Merge Sort:

Very predictable performance.

Stable sort (keeps equal elements in order).

Works great on linked lists.

Better for external sorting (e.g., huge files).

🏆 So Which Is Better?
✔ Use Quick Sort when:

You want best practical speed on average.

Memory is limited.

Data fits in memory.

You’re OK with worst-case O(n²) (or you use pivot optimization).

👉 Usually better for arrays in real-world use.

✔ Use Merge Sort when:

Stability is required.

You cannot tolerate worst-case O(n²).

Data is a linked list.

You are sorting huge data from disk (external sorting).

👉 Usually better for linked lists and guaranteed performance.
"""