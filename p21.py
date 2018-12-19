def collinear(x1, y1, x2, y2, x3, y3): 
    a = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2) 
  
    if (a != 0): 
        print "yes"
    else: 
        print "no"
  
# Driver Code 
x1, x2, x3, y1, y2, y3 = 0, 1, 0, 0, 0, 2
collinear(x1, y1, x2, y2, x3, y3) 
  
