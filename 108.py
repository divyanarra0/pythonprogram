def kthSmallest(arr, n, k): 
    arr.sort() 
    return arr[k-1] 
if __name__=='__main__': 
    arr = [1,2,3,4,5] 
    n = len(arr) 
    k = 3
print(kthSmallest(arr, n, k))
  
