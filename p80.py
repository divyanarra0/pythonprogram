def minDiff(arr, arr_size): 
    min_diff = arr[1] - arr[0] 
      
    for i in range( 0, arr_size ): 
        for j in range( i+1, arr_size ): 
            if(arr[j] - arr[i] < min_diff):  
                min_diff = arr[j] - arr[i] 
      
    return min_diff 
      
# Driver program to test above function  
arr = [1,2,3,4,5] 
size = len(arr) 
print ( minDiff(arr, size)) 
