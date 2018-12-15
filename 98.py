def printOrder(arr,n) : 
      
    # sorting the array 
    arr.sort() 
   
    # printing first half in ascending  
    # order 
    i = 0
    while (i< n/ 2 ) : 
        print arr[i], 
        i = i + 1
          
    # printing second half in descending  
    # order 
    j = n - 1
    while j >= n / 2 : 
        print arr[j], 
        j = j - 1
          # Driver code 
arr = [1,2,3,4,5,6,8] 
n = len(arr) 
printOrder(arr, n) 
