# Given an array, arr[] of n integers, and an integer element x, find whether element x is present in the array. Return the index of the first occurrence of x in the array, or -1 if it doesn't exist.

#     Input: arr[] = [1, 2, 3, 4], x = 3
#     Output: 2
#     Explanation: There is one test case with array as [1, 2, 3 4] and element to be searched as 3. Since 3 is present at index 2, the output is 2.


def linearsearch (arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i

    return -1

arr =[1,2,3,4,5,6]
x= 4
result = linearsearch(arr,x)

if result == -1:
    print('Element Not Found')
else:
    print('Element is present in index-',result, ', means', result+1, 'th position')