# making an array Ascending with Bubble Sorting

def ascending_bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        
        
        for j in range (n-1-i):
            
            # If elements are in wrong order -> swap manually
            if arr[j]>arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr [j+1] = temp
    return arr

arr = [5,2,8,1,7]
print('After sorting to an ascending order:', ascending_bubble_sort(arr))





    #---------My learnign understanding part----------
# Bubble Sort = Repeatedly walk through the list, compare two neighbors at a time, and swap them if they're in the wrong order. Keep doing this, and eventually the largest numbers "bubble" to the end.

# so starting from the 0th element of the array, we check left to right. and push the biggest element to the right most position at the very 1st pass. (if we start form n-1 th position then we do right to left and push the lowest value to the first position means left most position)

# Why for i in range(n-1)??
# "After each full pass(1 pass = full array check 1 time, neighour by neighour), one more number gets locked into its correct position at the end."
# So with 5 numbers → → the first 4 numbers are in correct order relative to each other, and the last one (which was already placed in pass 1) is also correct.
# So after 4 passes, the entire list is 100% sorted!

# Why for j in range(n - 1 - i)??
# In this pass, only compare the first (n - 1 - i) pairs —
# because the last i elements are already perfectly sorted and don’t need touching!

# What if we forgot the - i and always did range(n-1)?
# The code would still work correctly!
# But it would waste time doing useless comparisons at the end.
# So this - i saves time by skipping already-sorted elements at the end. (called optimization)

# temp: If I don’t use temp, I will lose one of the values forever. 
# If I write this (without temp):

# arr[j] = arr[j+1]   → arr[j] becomes 3
# arr[j+1] = arr[j]   → now I copy 3 again → arr[j+1] also becomes 3

# Result: [3, 3] → I lost the 5 forever!
# Both numbers became 3. Disaster!

