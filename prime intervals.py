l,h=map(int,raw_input().split())
for n in range(l,h+1):
    if n>1:
         for i in range(2,n):
             if(n%i)==0:
	      break
         else:
               print(n),
