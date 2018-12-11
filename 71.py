def reverse(str): 
    return str[::-1] 
 
def isPalindrome(str): 
 
    rev = reverse(str) 
 
    if (str == rev): 
        return True
    return False
str = "lappal"
ans = isPalindrome(str) 
 
if ans == 1: 
    print("Yes") 
else: 
    print("No") 
