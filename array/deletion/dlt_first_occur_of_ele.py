# Delete First Occurrence of Given Element from an Array

# Input: arr[] = [10, 20, 30, 20, 40], ele = 20
# Output: [10, 30, 20, 40]

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
    print('Target Element not found')
    print ('Not found. so array is-',*arr)


#---------My learnign understanding part----------
# (*arr) this is the way to print an array without its []