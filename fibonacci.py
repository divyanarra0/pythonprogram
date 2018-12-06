def f(n):
    if(n<=1):
        return n
    else:
        return (f(n-1)+f(n-2))
n=int(raw_input())
for i in range(1,n+1):
    print f(i),
