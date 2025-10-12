# Given an array of integers, the task is to delete an element from the beginning of the array.
# Input: arr[] = [10, 20, 30, 40]
# Output: [20, 30, 40]


arr = [10, 20, 30, 40]
n = len(arr)

for i in range(1, n, 1):
    arr[i - 1] = arr[i]
	
#arr.pop() # remove last duplicate element (Real deletion)
 
#  n-=1 #another way of sizing the array
# print('New Array:', *arr) #not possible by this way here cz arr is not cut short autometically

nx = len(arr)-1 ## I didn’t actually delete anything from arr, I just stopped printing the last element.

print("Array after deletion-")
for c in range(nx):
    print(arr[c], end=" ")
    
print('\n')
print(*arr[:nx]) #another way of printing
