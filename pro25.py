def lenOfLongIncSubArr(arr, n) : 
    m = 1 
    l = 1 
    for i in range(1, n) : 
        if (arr[i] > arr[i-1]) : 
            l =l + 1 
        else : 
            if (m < l)  : 
                m = l  
            l = 1 
    if (m < l) : 
        m = l 
    return m 
arr = [1,2,2,1,3] 
n = len(arr) 
print( lenOfLongIncSubArr(arr, n)) 
