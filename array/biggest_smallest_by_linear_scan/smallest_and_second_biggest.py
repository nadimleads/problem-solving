#Find the Smallest and the 2nd Buggest element of an array

def smallest_and_sec_biggest(arr):
    n = len(arr)
    smallest = arr[0]
    biggest = float('-inf')
    second_biggest = float('-inf')
    
    for x in range(n):
        if arr[x]<smallest:
            smallest=arr[x]
        
        if arr[x] > biggest:
            second_biggest = biggest
            biggest = arr[x]

# its saying that "if the currant element you are checking is bigger than second biggest then make it the second biggest" then additionally I added "and if current element is not equal to the biggest then make it the second biggest" so that duplicate biggest doesn't get printed as 2nd Biggest!!
        elif arr[x]>second_biggest and arr[x] != biggest:
            second_biggest = arr[x]
            
    return smallest,biggest, second_biggest

arr = [1001,1001,11,112,123,143,115,1000,16,7,128,199,1000,1001,1001,5,8,8,2,2,2,12,5,99]
smallest_value, biggest_value, second_biggest_value = smallest_and_sec_biggest(arr)

print("Smallest value:", smallest_value)
print("2nd Biggest value:", second_biggest_value)






#---------My learnign understanding part----------
# float('inf')
# = positive infinity → bigger than all numbers
# (we use this when finding minimums)

# ✔ float('-inf')
# = negative infinity → smaller than all numbers
# (we use this when finding maximums)