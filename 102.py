def divide(dividend, divisor):  
    sign = -1 if ((dividend < 0) ^  (divisor < 0)) else 1
    dividend = abs(dividend) 
    divisor = abs(divisor)
    quotient = 0
    while (dividend >= divisor):  
        dividend -= divisor 
        quotient += 1
    return sign * quotient 
a = 1
b = 1
print(divide(a, b)) 
