# making an array Descending with Insertion Sorting

def descending_insertion(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i] # taking one (starting from 2nd one) element which gonna be shifted
        j = i - 1 # keeping previous element's INDEX in hand for comparing later

        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j = j - 1  #j -= 1
        arr[j+1] = key #Best OPTIMIZED way

    return arr

arr = [5,2,8,1,7]
print(descending_insertion(arr))