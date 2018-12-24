def isSum(a11,b11,c11):
    if b11<c11:
        c11,b11=b11,c11
    while a11>=0:
        if a11%b11==0:
            return True
        a11-=c11
    return False
a11 = int(input())
if isSum(a11,3,7):
    print("yes")
else:
    print("no")
