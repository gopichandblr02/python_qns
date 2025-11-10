### python_tips

#### 1. Tips for loops
- arr=  [1,2,3,4,5,6]
- Index  0,1,2,3,4,5
- Here length = 6, last_element = arr[-1] or arr[5] or arr[arr_length-1]
```
for x in range(arr_len):
    print(arr[x])
```
- To skip first element
```
for x in range(1,arr_len):
    print(arr[x])
```
or
```
for x in arr[1:]:
    print(x)
```

- Reverse
```
arr=[16, 17, 4, 3, 5, 2]
a = arr[-1:0:-1] or arr[-1::-1] or arr[::-1]
print(a)
```

