p11=raw_input()
a=len(p11)
s=list(p11)
if a%2==0:
    m=a/2 - 1
    s[m]='*'
    s[m+1]='*'
else:
    m=a/2 - 1
    s[m+1]='*'
print "".join(s)
