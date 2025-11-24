# Find the Smallest, 2nd Smallest and the 3rd Smallest value from the array (no duplicate allowed)

def smallest_and_second_smallest(arr):
    n= len(arr)
    smallest = float('inf')
    second_smallest = float('inf')
    third_smallest = float('inf')
    
    for x in range(n):

        if arr[x]<smallest:
            second_smallest = smallest
            smallest = arr[x]

        elif arr[x] < second_smallest and arr[x] != smallest:
            second_smallest = arr[x]
        
        elif arr[x] > second_smallest and arr[x] < third_smallest and arr[x] != second_smallest :
            third_smallest = arr[x]

    return smallest,second_smallest, third_smallest

arr = [11,112,11,123,143,115,16,7,7, 128,199,1000, 1001, 5, 8,8,2,2,2, 12,5, 99]
smallest_value, second_smallest_value, third_small_value = smallest_and_second_smallest(arr)

print("Smallest value:", smallest_value)
print("2nd Smallest value:", second_smallest_value)
print("3nd Smallest value:", third_small_value)



#---------My learnign understanding part----------

# float('inf') means infinity — a very very(infinity) large number.
# smallest = ∞
# second_smallest = ∞
# Because ANY real number in the array will be smaller than ∞.
# So the first element will automatically become the smallest.

# “If I find a new smallest number,
# then the old smallest becomes the second smallest.”
# 11 < ∞ → true
# second_smallest = ∞
# smallest = 11


# elif arr[x] < second_smallest and arr[x] != smallest:
#             second_smallest = arr[x]
# its saying that "if the currant element you are checking is smaller than second smallest then make it the second smallest" then additionally I added "and if current element is not equal to the smallest then make it the second smallest" so that duplicate smallest doesn't get printed as 2nd smallest!!

# “If I find a new smallest number,
# then the old smallest becomes the second smallest.”
# If the number is bigger than the smallest
# but still smaller than the second smallest,
# update second smallest.”
# 112 is not < smallest (11)  
# 112 < ∞ → true  
# → second_smallest  112