arr = [1, 4, 3, 2, 6, 5]
arr_len=len(arr)
temp=[0]*arr_len
for i in range(arr_len):
    temp[-i-1]=arr[i]
print(*temp,sep=" ")