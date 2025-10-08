# Given an array of integers, the task is to delete an element from the beginning of the array.
# Input: arr[] = [10, 20, 30, 40]
# Output: [20, 30, 40]


arr = [10, 20, 30, 40]
n = len(arr)

for i in range(1, n, 1):
    arr[i - 1] = arr[i]
	
#  n-=1 #another way
# print('New Array:', *arr) #no possible by this way here cz arr is not cut short autometically


nx = len(arr)-1 ## cut size by 1 in the back


print(*arr[:nx]) #another way

print("Array after deletion-")
for i in range(nx):
    print(arr[i], end=" ")
