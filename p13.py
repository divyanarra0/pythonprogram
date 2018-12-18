p11=int(input())
sum=0
while(p11>0):
    n=int(p11%10)
    sum=(n*n)+sum
    p11=int(p11/10)
print(sum)
