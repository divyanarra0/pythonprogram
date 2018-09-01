num=int(input(""))
temp=num
rev=0
while(temp>0):
	rem=temp%10
	rev=rev+rem*rem*rem
	temp//=10
if num==rev:
	print"yes"
else:
	print"no"
