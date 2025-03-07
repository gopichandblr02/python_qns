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