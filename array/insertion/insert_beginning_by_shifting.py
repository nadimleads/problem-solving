# Given an array of integers, the task is to insert an element at the beginning of the array.
# first shift all the elements of the array to the right by 1 index and after shifting insert the new element at 0th position.

# Input: arr[] = [10, 20, 30, 40], ele = 50
# Output: [50, 10, 20, 30, 40]

array =[10,20,30,40]
elemet = 50
n= len(array) #4

new_array= array +[0] # Increase size of array

for i in range (n-1,-1,-1):
    new_array[i+1] = new_array[i]
    print(new_array) #just to see

new_array[0]=elemet

print('\n','Insert 50 at the beginning(raw array print):',new_array)

print('\n','Insert 50 at the beginning(using prebuilt *system):',*new_array)

print("\nInsert 50 at the beginning(showing with loop):")
for new in range(n+1):
    print(new_array[new], end=" ")

