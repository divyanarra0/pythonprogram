def fillsuffixSum(arr, n, suffixSum): 
    suffixSum[0] = arr[0] 
    for i in range(1, n): 
        suffixSum[i] = suffixSum[i - 1] + arr[i] 
arr =[1,1,1,1,1 ] 
n = len(arr) 
suffixSum = [0 for i in range(n + 1)] 
fillsuffixSum(arr, n, suffixSum) 
for i in range(n): 
    print(suffixSum[i]), 
