def runnigsum(arr):
    n=len(arr)
    for i in range(1,n):
        arr[i] = arr[i-1]+arr[i]
    return arr[n-1]

numbers=[1,2,3,4,5,6,7]
print(runnigsum(numbers))