# Given an array of integers, the task is to delete an element from a given position in the array.
# Input: arr[] = [10, 20, 30, 40], pos = 2
# Output: [10, 30, 40]

arr= [10, 20, 30, 40]
pos=2
n= len(arr)

if pos <= 0 or pos > n:
    print("Invalid Input")
else:
    for i in range(pos, n):
        arr[i-1] = arr[i]
        print(arr)
    
    nx = len(arr)-1

    print("Array after deletion-")
    for k in range(nx):
        print(arr[k], end=" ")
    
    
# Using pos= 4 That means start at 4(i=4), stop before 4.
# So, this loop never runs even once.
# There’s no iteration at all — the for body never executes.
# That’s why no error occurs.