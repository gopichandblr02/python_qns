## reverse

a =123456
ans=0
while a:
    ans = ans*10+a%10
    a//=10
print(ans)