def func(arr,tar):
    seen={}
    for i,ele in enumerate(arr):
        rem = tar-ele
        if rem in seen:
            return (i,seen[rem])
        else:
            seen[ele]=i

print(func([2,3,4],6))