n11,m11=map(int,raw_input().split())
if n11>m11:
    s=n11-m11
else:
    s=m11-n11
if s%2==0:
    print "even"
else:
    print "odd"
