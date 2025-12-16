#Binary Search (Recursive)
# An array MUST BE sequentially sorted for the binary search algorithm to function correctly.

# Given an array, arr[] of n integers, and an integer element x, find whether element x is present in the array. Return the index of the first occurrence of x in the array, or -1 if it doesn't exist.

# Recursive: A function calls itself to solve smaller sub-problems of the same type until a base condition is reached.
#Useful for: Problems naturally defined in smaller sub-problems (divide-and-conquer, trees, graphs)

def binary_recursive(arr, low, high, target):
    if high >= low:
        mid = low + (high - low) // 2 # floor division removes the decimal value

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_recursive(arr, low, mid - 1, target)
        else:
            return binary_recursive(arr, mid + 1, high, target)
    else:
        return -1

arr = [11, 12, 13, 14, 15, 16, 17, 19, 18, 19] 
target = 19
n = len(arr)

result = binary_recursive(arr, 0, n - 1, target)

if result != -1:
    print('Target found at index:', result, ', means:', result + 1, 'nd position')
else:
    print('Target not here')