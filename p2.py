Num1 = int(raw_input())
Reverse = 0
while(Num1 > 0):
	Reminder = Num1 %10
	Reverse = (Reverse *10) + Reminder
	Num1 = Num1 //10.
print("%d" %Reverse)
