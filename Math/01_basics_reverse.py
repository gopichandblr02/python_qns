a=b=123456
rev=0
while a:
    rev=rev*10+a%10
    a//=10

print(rev)
new_rev=0
while b>new_rev:
    new_rev=new_rev*10+b%10
    b//=10
print("----")
print(b)
print(rev)

# 654321
# ----
# 123
# 654321