p11=int(raw_input())
s=[]
while(p11>0):
    dig=p11%10
    s.append(dig)
    p11=p11//10
print sum(s)
