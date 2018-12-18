p11,k=map(int,raw_input().split())
p11=int(p11)
k=int(k)
         
if p11 > k: 
    small = k
else: 
    small = p11 
for i in range(1, small+1): 
    if((p11 % i == 0) and (k % i == 0)): 
        gcd = i 
print(gcd) 
