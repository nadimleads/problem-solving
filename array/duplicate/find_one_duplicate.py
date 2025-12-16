# Find One duplicate: Given an array, find any ONE element that appears more than once.
def find_one_duplicate(arr):
    n= len(arr)
    
    for i in range(n-1):
        for j in range(i+1,n):
            if arr[i] == arr[j]:
                return arr[i]
            
    return -1

arr = [11, 12, 13, 14, 15, 16, 17, 19, 18,19, 19] 
result = find_one_duplicate(arr)

if result!=-1:
    print(result)
else:
    print('There is not a single Duplicate!')


#---------My learnign understanding part----------
# “When I look at a value, have I already seen it before?” That’s the only thing you need to know.
# Raise your hand as soon as you see any two students with same roll

# Return the value When I see a same value again
# Stop Immediately
# Return “no duplicate” if no duplicate found(or -1 / None)