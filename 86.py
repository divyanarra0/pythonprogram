def isIsogram(p11):
	charMap = {}
	for q in p11:
		if q in charMap:
			return False
		else:
			charMap[q] = 1
	return True
p11 = raw_input().rstrip()
print("Yes" if isIsogram(p11) else "No")
