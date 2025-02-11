#

a =[-1,10,-2,200]
max_sum=a[0]
for i in range(len(a)):
    for j in range(i,len(a)):
        max_sum = max(max_sum,sum(a[i:j+1]))
print(max_sum)

# single loop ??


