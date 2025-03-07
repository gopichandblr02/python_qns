def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    left_half=merge_sort(arr[:mid])
    right_half=merge_sort(arr[mid:])
    return merge(left_half,right_half)

def merge(left,right):
    i=j=0
    final_arr=[]
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            final_arr.append(left[i])
            i+=1
        else:
            final_arr.append(right[j])
            j+=1
    final_arr.extend(left[i:])
    final_arr.extend(right[j:])
    return final_arr

if __name__=="__main__":
    arr = [10,7,8,9,1,5]
    print(merge_sort(arr))