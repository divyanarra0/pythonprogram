s11=int(raw_input())
digits = []
while s11 > 0:
    r = s11 % 10
    if r & 1 != 0:
        digits.append(str(r))
    s11=s11/10
digits = reversed(digits)
print (" ".join(digits))
