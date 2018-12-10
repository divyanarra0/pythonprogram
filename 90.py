a11 = raw_input().rstrip()
digits = []
for p in a11:
	if p.isdigit():
		digits.append(p)
print("".join(digits))
