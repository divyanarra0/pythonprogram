def findK(n, k): 
    half = int((n + 1) / 2) 
    if k > n: 
        return (2 * (k - half)) 
    else: 
        return (2 * k - 1) 
n = 5
k = 3
print(findK(n, k)) 
