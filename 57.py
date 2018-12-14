a1,b1=map(int,raw_input().split())
list=[int(x) for x in raw_input().split()]
if b1 in list:
    count=list.count(b1)
    print count
else:
    print 0
