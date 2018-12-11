import math
s11,m11=map(int,raw_input().split())
a=s11 * m11
if math.sqrt(a).is_integer():
    print "yes"
else:
    print "no"
