n,m=map(int,raw_input().split())
if n>m:
    c=n-m
else:
    c=m-n
if c%2==0:
    print "even"
else:
    print "odd"
