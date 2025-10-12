arr = [1,2,2,5,4]
n= len(arr)
ele=2

new_len= 0

for i in range(n):
    if arr[i] != ele:
        arr[new_len] = arr[i]
        new_len = new_len+1
        
# arr[i] == ele: Using this logic, that if element matches with the ele, then kick the eles out
# for i in range(n):
#     if arr[i] == ele:
#         continue
#     else:
#         arr[new_len] = arr[i]
#         new_len = new_len+1

print('After deducting all occurance, I have',new_len,'items left') #showing the number of elements left in after removing all occurrance
for j in range (new_len):
    print(arr[j], end=' ')
    
print("\nArray after deletion:", *arr[:new_len]) #Print all values without loop





