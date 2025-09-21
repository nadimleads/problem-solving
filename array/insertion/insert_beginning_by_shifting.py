# Given an array of integers, the task is to insert an element at the beginning of the array.
# first shift all the elements of the array to the right by 1 index and after shifting insert the new element at 0th position.

# Input: arr[] = [10, 20, 30, 40], ele = 50
# Output: [50, 10, 20, 30, 40]

array =[10,20,30,40]
elemet = 50
n= len(array)

array= array +[0] # Increase size of array

for i in range (n-1,-1,-1):
    array[i+1] = array[i]
    print(array) #just to see

array[0]=elemet
print('\n','Insert 50 at the beginning:',*array)

