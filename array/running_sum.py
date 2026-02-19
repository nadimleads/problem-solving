# 1. Running Sum of an array (modifying the same array)
print('Running Sum of an array (modifying the same array)')

def running_sum_mod(arr):
    n= len(arr)

    for i in range(1, n):
        arr[i] = arr[i-1] + arr[i]

    return arr

arr= [1, 2, 3, 4, 5]
print(running_sum_mod(arr))


# 2. Running Sum of an array (Using another array so that the main array is untouched)
print('Running Sum of an array (Using another array so that the main array is untouched)')

def running_sum(arr):
    n= len(arr)
    result = [0] * n
    
    result[0] = arr[0]

    for i in range(1, n):
        result[i] = result[i-1] + arr[i]

    return result

arr= [1, 2, 3, 4, 5]
print(running_sum(arr))


# 3. Running Sum of an array (without using method def)
print('Running Sum of an array (without using method def)')

arrx= [1,2,3,4,11]
n = len(arr)
for i in range(1,n):
    arr[i] = arr[i-1]+ arr[i]

print(*arr)

# 4. Show ONLY the final total instead of the whole running-sum array.
print('Show ONLY the final total instead of the whole running-sum array.')
def running_sum_mod(arr):
    n= len(arr)

    for i in range(1, n):
        arr[i] = arr[i-1] + arr[i]

    return arr[n-1]

arr= [1, 2, 3, 4, 5]
print(running_sum_mod(arr))

# 5. running-sum array counting from back(Right to left).
print('running-sum array counting from back(Right to left)')

def running_sum_mod(arr):
    n= len(arr)

    for i in range(n-2, -1,-1): # start from second last
        arr[i] = arr[i+1] + arr[i]  #add the element on the right

    return arr,arr[0]

arr= [1, 2, 3, 4, 5]
print(running_sum_mod(arr))


# 6. n(n+1)/2 BUT still involve an array (testing).
print('n(n+1)/2 BUT still involve an array (testing).')
arr = [1,2,3,4,5,6,7,8,9,10]

n = len(arr)
total = n * (n + 1) // 2

print(total)




#---------My learnign understanding part----------
#      if I do result = arr?
# arr and result → both names pointing to the exact same array in memory
# So any change to result will ALSO modify arr.
# This destroys your original array.

# n * (n + 1) // 2
# This formula only works IF the array is a perfect sequence starting from 1.
# It will NOT work for something like:[2,5,8]