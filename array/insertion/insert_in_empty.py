# Given an array of integers, the task is to insert an element at the beginning of the array.
# first shift all the elements of the array to the right by 1 index and after shifting insert the new element at 0th position.

# Input: arr [] = [], ele = 50
# Output: [50]

arr=[]
ele=50
arr_new=arr+ [0]
arr_new[0]=ele
print(*arr_new)


