low11,upp11=map(int,raw_input().split())
count=0
for num in range(low11,upp11+1):
    if num>1:
        for x in range(2,num):
            if(num%x==0):
                break
        else:
          count=count+1
print (count) 
