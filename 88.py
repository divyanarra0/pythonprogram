p1,q1=map(int,raw_input().split())
if(p1>q1):
    min1=p1
else:
    min1=q1
while(1):
    if(min1%p1==0 and min1%q1==0):
        print(min1)
        break
    min1=min1+1

