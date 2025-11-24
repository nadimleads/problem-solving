#Find the Biggest and the Smallest Value of an Array

def min_max_value(arr):
    max = arr[0]
    min = arr[0]
    n = len(arr)
    
#Using index
    for x in range(n):
        if arr[x] > max:
            max = arr[x]

        if arr[x] < min:
            min = arr[x]

    return max, min

arr = [11,112,123,143,115,16,7,128,199]
max_value, whatever_name_mainimum = min_max_value(arr) #tuple unpacking for seperate print from one function

print("Smallest value:", whatever_name_mainimum)
print("Largest value:", max_value)



#---------my learnign understanding part----------
# tuple is an ordered collection of multiple data elements, used in programming and mathematics. It is similar to a list, but once created, its elements cannot be changed.

#Using array element directly (Python)
    # for y in arr:
    #     if y>max:
    #         max = y

    #     if y<min:
    #         min = y
    # return max, min