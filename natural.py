num=int(input(""))
if(num<0):
	print("the num is negative")
elif(num==0):
	print("the num is zero")
else:
	num=num*(num+1)/2
print(num)
