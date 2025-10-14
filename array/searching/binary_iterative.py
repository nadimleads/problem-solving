# arr = [11,12,13,14,15,16,17,18,19]
# length = 9 (0-8)

def binaryiterative (arr, target):
    n= len(arr)
    low = 0
    high = n-1
    
    while low <= high:
        mid = low + (high-low)//2
        
        if arr[mid] == target:
            return mid
        
        elif arr[mid]>target:
            high= mid-1
        else:
            low= mid+1
    
    return -1

arr = [11,12,13,14,15,16,17,18,19]
target = 19
result= binaryiterative(arr,target)

if result != -1 and arr[result] == target:
    print('Target found at index:', result, ', means:',result+1,'nd position')
else:
    print('Target not here')
