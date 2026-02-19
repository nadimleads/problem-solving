#reverse an array

arr= [2,3,4,5,6,7]
n= len(arr) #6 (0-5)

for i in range (n-1,-1,-1):
    # This If check is just for using comma
    if (arr[i] == arr[0]):
        print(arr[i],end='')
    else:
        print(arr[i],end=',')


# Another way

def print_reverse(arr):
    n = len(arr)
    
    for i in range(n - 1, -1, -1):
        print(arr[i], end='')


arr = [2, 3, 4, 5, 6, 7]
print_reverse(arr)