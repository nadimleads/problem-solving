# Count and Find only the UNIQUE items in an array(An item that appears exactly ONCE in the array)

def yo(arr):
    n=len(arr)
    arr_new=[0]*n
    position=0

    for i in range(n):
        for j in range(n):
            if i!=j:
                if arr[i]!=arr[j]:
                    notduplicate = True
                else:
                    notduplicate = False
                    break
        if notduplicate:
            arr_new[position] = arr[i]
            position = position+1
    
    if position == 0:
        return -1
    else:
        result = [0] * position
        for x in range(position):
            result[x] = arr_new[x]
        return result, position


arr = [2, 2, 3, 4, 5, 5, 4, 3] # all duplicate
# arr = [3, 2, 4, 5, 2] # Dining tabe try
output= yo(arr)
total_items = len(arr)

if output!=-1:
    unique_items, unique_count = output
    duplicate_count = total_items - unique_count
    print("Total items:", total_items)
    print("Total unique (single) items:", unique_count)
    print("Total duplicate items:", duplicate_count)
    print("Unique items are:", unique_items)
else:
    print("Total items:", total_items)
    print("There are no unique items. All are duplicates.")



    #---------My learnign understanding part----------
# If a problem asks “appears exactly once”, stop thinking in pairs. Start thinking in counts.

# For pair-based problems (duplicates, comparisons, sorting):

    # You only need to compare pairs
    # Once all pairs are checked, you’re done
    # Last element doesn’t need to “start” a comparison
    # So i can safely go up to n-2
    # ✔ That’s why range(n-1) is fine there

# For count-based problems (unique = appears exactly once):

    # Each element must be evaluated as a candidate
    # Even the last element might be unique
    # Uniqueness is about global count, not pairs
    # ✔ So every element must be “picked” once

            # REMEMBER THIS DEAR MEE
# If the decision depends on “not found anywhere”, NEVER put else or if inside the loop.

# MOST BASIC STRUCTURE compare an element of an array with all other element of the same array
    # ✔ Every element compared with all others
    # for i in range(n):
    #     for j in range(n):
    #         if i != j:
    #             # compare arr[i] with arr[j]


        # Refined loop (same logic, much cleaner)
    # for i in range(n):
    #     for j in range(n):
    #         if i != j and arr[i] == arr[j]:
    #             break   # duplicate found
    #     else:
    #         # this runs ONLY if no break happened
    #         arr_new[position] = arr[i]
    #         position += 1
    
    
        # Refined version (NO boolean flag)
    # for i in range(n):
    #     notduplicate = True   # assume unique for this i

    #     for j in range(n):
    #         if i != j and arr[i] == arr[j]:
    #             notduplicate = False
    #             break   # no need to check further

    #     if notduplicate:
    #         arr_new[position] = arr[i]
    #         position += 1