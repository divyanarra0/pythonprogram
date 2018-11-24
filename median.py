l = int(raw_input())
number = [1,2,3,4,5]
number .sort()
l = len(number)
if (l  % 2 == 0):
    median = (number[(l)//2] + number[(l)//2-1]) / 2
else:
    median = number[(l-1)//2]
print(median)
