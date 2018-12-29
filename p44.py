def rat(k11,n11):
    print(k11[n11:]+k11[:n11])
k11,n11=map(str,raw_input().split())
n11=int(n11)
m=len(k11)-n11
rat(k11,m)
