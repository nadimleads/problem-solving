#delete an elment from the end of the array

arr = [10, 20, 30, 40]
n = len(arr)

nx = len(arr)-1 ## I didn’t actually delete anything from arr, I just stopped printing the last element.

print("Array after deletion from end-")
for i in range(nx):
    print(arr[i], end=" ")