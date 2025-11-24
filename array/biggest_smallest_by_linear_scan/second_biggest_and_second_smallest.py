# Find the biggest and 2nd Biggest then the smallest and the 2nd Smallest value from the array (no duplicate allowed)

def secondBiggest_and_secondSmallest(array):
    n= len(array)
    biggest= float('-inf')
    sec_biggest= float('-inf')
    smallest=float('inf')
    sec_smallest=float('inf')
    
    for b in range(n):
        if array[b]>biggest:
            sec_biggest=biggest
            biggest=array[b]
        elif array[b]>sec_biggest and array[b]!=biggest:
            sec_biggest=array[b]
        
        if array[b]<smallest:
            sec_smallest=smallest
            smallest=array[b]
        elif array[b]<sec_smallest and array[b]!=smallest:
            sec_smallest=array[b]

    return biggest,sec_biggest,smallest,sec_smallest

array = [1001, 1001, 105, -500, -500, -50, 105, 12, -88, 77, 12, 0, -1, 99, 77, -88, 200, 200, 15]
biggest_value,biggest2_value,smallest_value,smallest2_value = secondBiggest_and_secondSmallest(array)

print("Biggest value:", biggest_value)
print("2nd Biggest value:", biggest2_value)
print("Smallest value:", smallest_value)
print("2nd Smallest value:", smallest2_value)





    #---------My learnign understanding part----------
# float('inf')
# = positive infinity → bigger than all numbers
# (we use this when finding minimums)

# float('-inf')
# = negative infinity → smaller than all numbers
# (we use this when finding maximums)


# Using Element Method in pythonic way

# for b in array: 
#         if b > biggest:
#             sec_biggest = biggest
#             biggest = b
#         elif b > sec_biggest and b != biggest:
#             sec_biggest = b
            
       
#         if b < smallest:
#             sec_smallest = smallest
#             smallest = b
#         elif b < sec_smallest and b != smallest: 
#             sec_smallest = b