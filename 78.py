def isMultipleOf13(n): 
  
    odd_count = 0
    even_count = 0
  
    # Make no positive if +n is multiple of 13 
    # then is -n. We are doing this to avoid 
    # stack overflow in recursion 
    if(n < 0):  
        n = -n 
    if(n == 0): 
        return 1
    if(n == 1):  
        return 0
  
    while(n): 
          
        # If odd bit is set then 
        # increment odd counter  
        if(n & 1):  
            odd_count += 1
        n = n >> 1
  
        # If even bit is set then 
        # increment even counter  
        if(n & 1): 
            even_count += 1
        n = n >> 1
  
    return isMultipleOf13(abs(odd_count - even_count)) 
  
# Program to test function isMultipleOf13  
num = 5
if (isMultipleOf13(num)):  
    print('yes') 
else: 
    print('no') 
  
