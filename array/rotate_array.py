# Rotate an Array (Simple opotimized way)

def rotate_arr(arr):
    n= len(arr)
    first = arr[0]
    
    for i in range(1,n):
        arr[i-1] = arr [i]
        
    arr[n-1]= first
    return arr

arr= [1,2,3,4,5,6,7,8,9]
print(rotate_arr(arr))

# dear me, lesson is in 'rotate_array_experiment' file