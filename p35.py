p11=str(raw_input())
N2=str(p11.lower())
p=[]
for x in N2:
    if(N2.count(x)==1):
        p.append(x)
N1=" ".join(map(str,p))
print(N1)
