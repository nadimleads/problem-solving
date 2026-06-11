#delete an elment from the end of the array

arr = [10, 20, 30, 40]
n = len(arr)

nx = len(arr)-1 ## I didn’t actually delete anything from arr, I just stopped printing the last element.

print("Array after deletion from end-")
for i in range(nx):
    print(arr[i], end=" ")
    
    
    
def removefromback(array):
    newbox=[0]* (len(array)-1) #
    
    i=0
    while i < (len(array)-1):
        newbox[i]=array[i]
        i=i+1
    
    return newbox
    
List=[1,2,3,4,5,6,6,5,7,8]
print(removefromback(List))