#Delete all occurance of the "given element" from an array (all duplicate of given item)

arr = [1,2,2,5,3,3,6,4]
n= len(arr)
ele=2

new_len= 0

for i in range(n):
    if arr[i] != ele:
        arr[new_len] = arr[i]
        new_len = new_len+1

# Using this logic, that if element matches with the ele, then kick the given eles out
# arr[i] == ele: 

# for i in range(n):
#     if arr[i] == ele:
#         continue
#     else:
#         arr[new_len] = arr[i]
#         new_len = new_len+1

print('After deducting all occurance of', ele, ',I have',new_len,'items left') #showing the number of elements left in after removing all occurrance

#Print values with for loop
print('using loop:',end=' ')
for j in range (new_len):
    print(arr[j], end=' ')

print("\nArray after deletion(pythonic style):", *arr[:new_len]) #Print all values without loop