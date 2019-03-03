def checkValidity(a1, b1, c1):  
    if (a1 + b1 <= c1) or (a1 + c1 <= b1) or (b1 + c1 <= a1) : 
        return False
    else: 
        return True
a1 = 3
b1 = 4
c1 = 5
if checkValidity(a1, b1, c1): 
    print("yes")  
else: 
    print("no") 
