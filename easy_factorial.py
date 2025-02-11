###### factorial using for loop
def factorial(n):
    fact=1
    for _ in range(0,n):
        fact = fact*(_+1)
    return fact
print(factorial(5))

###### factorial using while loop
def factorial_while(n):
    fact=n
    while n>1:
        fact = fact*(n-1)
        n-=1
    return fact
print(factorial_while(5))
