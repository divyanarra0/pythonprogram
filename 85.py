a11 = raw_input().rstrip()
evenS = odda11 = ''
for i, p in enumerate(a11):
	if i & 1 == 0:
		evenS += p
	else:
		odda11 += p
 
print(evenS + " " + odda11)
