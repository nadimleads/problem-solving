# Given an array of integers, the task is to insert an element at the beginning of the array.

# Input: arr [] = [], ele = 50
# Output: [50]

arr=[]
ele=50
arr_new=arr+ [0]

arr_new[0]=ele
print(*arr_new)