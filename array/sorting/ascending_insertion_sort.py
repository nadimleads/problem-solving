# making an array Ascending with Insertion Sorting

def Insertion_sort(arr,arr2):
    n = len(arr)
    for i in range(1, n):
        key = arr[i] # taking one (starting from 2nd one) element which gonna be shifted
        j = i - 1 # keeping previous element's INDEX in hand for comparing later

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1  #j -= 1
        arr[j+1] = key #Best OPTIMIZED way
    
    for i in range(1, len(arr2)):
        key = arr2[i]
        j = i - 1
        
        while j >= 0 and arr2[j] > key:
            arr2[j + 1] = arr2[j]
            j -= 1
            arr2[j + 1] = key # works totally fine but not optimized

    return arr, arr2

# Example
arr = [5,2,8,1,7]
arr2 = [4, 3, 2, 10, 12, 1, 5]
print(Insertion_sort(arr,arr2))





    #---------My learnign understanding part----------
# Insertion Sorting: Its like I am playing card and I pick up cards one by one and keep them sorted in my hand.

# Insertion Sort: Take one element and insert it into its correct place in the correctly sorted part. It is most practical for small data, [Take each new number, and slide all the bigger numbers in the sorted part one step to the right until you find the correct place to insert it.]

#       Why for i in range(1, n) → start from 1, not 0?
#  Because the we take the first element (index 0) as already "sorted by itself"..then form the 2nd element (index 1) We only compare and shift with the LEFT side (the already-sorted part).

#       while j >= 0 and arr[j] > key why?
#  j >= 0 → if index goes to -1 or 0 more than left end of the array
#  arr[j] > key → The element on the left is bigger than our key
#  (so it needs to move right to make space)

#       Why “while” is required (real reason)?
#  Insertion sort must:
#  Keep shifting values
#  Keep comparing
#  Keep moving
#  Until it finds a position where arr[j] <= key
# This means it needs a loop that repeats again and again.

            #Importat lesson NOTE#
# while j >= 0 and arr2[j] > key:
#             arr2[j + 1] = arr2[j]
#             j -= 1
#             arr2[j + 1] = key
# arr2[j + 1] = key, keeping this inside while loop is totally fine, no output error I found in many text cases, Also I wrote the full iteration in my notebook menually to see whats the issue. I think the main problem of keeping that line inside 'while' is making the code work more,which is for no reason, which is not an optimized way. cz the key gets inserted every time of the iteration of the while loop executes, which in not needed, cz it works perfectly if the key gets inserted to its position when each for loop iteration is finishing and also all "while loop's" iteration is completed inside 1 for loop iteration.
# SO, the main problem If I write it this way is "OPTIMIZATION", but it gives perfect output for almost all test cases I tried.