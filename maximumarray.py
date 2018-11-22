maximum = int(raw_input())
def largest(arr,n):
    maximum = arr[0]
    for i in range(1, n):
        if arr[i] > maximum:
            maximum = arr[i]
    return maximum
arr = [1,2,3]
n = len(arr)
Ans = largest(arr,n)
print (Ans)
