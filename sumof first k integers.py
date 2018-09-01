n,k=map(int,raw_input().split())
list=[int(x) for x in raw_input().split()]
s=0
for i in range(0,k):
	s=s+list[i]
print(s)
