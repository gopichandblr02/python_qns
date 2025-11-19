x =23/10   # 2.3
y=23//10   # 2  floor
a=321%10   # 1
print(1//10)  # 0
print(1%10)  # 1
print(1/10)  # 0.1
aa =1234
while aa:
    print(aa)
    aa=aa//10

for x in [1,2,8]:
    print(x)
# 1
# 2
# 8

# sep wont work for loops, it works for unpacking
for x in [1,2,8]:
    print(x,sep=";")
# 1
# 2
# 8

# Default separator is space
a=[1,2,3]
print(*a,sep=";")
# 1;2;3

# By default end is \n for loops
for x in a:
    print(x,end=",")
# 1,2,3,


print(10,20,30,sep=";")
# Output
#10;20;30

