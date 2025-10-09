# Delete First Occurrence of Given Element from an Array

# Input: arr[] = [10, 20, 30, 40], ele = 20
# Output: [10, 30, 40]

# Input: arr[] = [10, 20, 30, 40], ele = 25
# Output: [10, 20, 30, 40]

# Input: arr[] = [10, 20, 20, 30, 40], ele = 20
# Output: [10, 20, 20, 30]

arr = [10, 20, 30, 20, 40]
ele = 20
n = len(arr)
found = False

# traverse for searching ele
for i in range(n):
    if arr[i]== ele:
        found = True
        break

if found:
    for j in range(i, n-1):
        arr[j] = arr[j+1]
    
    nx = len(arr)-1

    print("Array after deletion of target occurance-")
    for x in range(nx):
        print(arr[x], end=" ")
else:
    print('Ele not found')
    print ('Not found. so-',*arr)