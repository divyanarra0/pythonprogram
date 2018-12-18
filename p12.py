_,NN = map(int,raw_input().split(" "))
data11 = map(int,raw_input().split(" "))
l = len(data11)
for __ in range(NN):
    data11 = [data11[l-1]] + data11[0:l-1]
print " ".join(map(str,data11))
