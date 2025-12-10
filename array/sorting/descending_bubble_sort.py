# making an array Descending with Bubble Sorting

def descending_bubble(arr):
    n= len(arr)
    
    for i in range(n-1):

        for j in range(n-1-i):

            if arr[j]<arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    
    return arr

arr = [5,2,8,1,7]
print('After sorting to an descending order:', descending_bubble(arr))