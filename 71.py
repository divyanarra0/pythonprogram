def reverse(str): 
    return str[::-1] 
  
def isPalindrome(str): 
 
    rev = reverse(str) 

    if (str == rev): 
        return True
    return False
str = "laptop"
ans = isPalindrome(str) 
  
if ans == 1: 
    print("yes") 
else: 
    print("no") 
