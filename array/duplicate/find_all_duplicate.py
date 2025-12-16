# Find All Duplicate values ONLY (brute-force Algorithm, triple-nested-loop approac)

def finde_duplicate(arr):

    n = len(arr)
    new_arr = [0] * n
    pos = 0  # next position to insert duplicate

    for i in range(n-1):
        for j in range(i + 1, n):
            if arr[i] == arr[j]:

                # check if already stored
                already_added = False
                for k in range(pos):
                    if new_arr[k] == arr[i]:
                        already_added = True
                        break

                if not already_added:
                    new_arr[pos] = arr[i]
                    pos += 1

    if pos>0:
        result = [0]*pos # just to make it array style like, [3,5,2]
        for x in range(pos):
            result[x]= new_arr[x]
        return result  #if i make it, not def method style then instead return, print should work
    else:
        return -1


arr = [3, 5, 3, 2, 5, 1, 5, 5, 2]
# arr = [3, 5, 4]
output= finde_duplicate(arr)

if output!=-1:
    print(output)
else:
    print('There is not a single Duplicate!')



#---------My learnign understanding part----------
# Consider this array:
# [1, 2, 3, 2, 4, 1]
# The duplicates are 2 (appears twice) and 1 (appears twice).
# Unique elements are 3 and 4.

# YES. You are Right
# The main difference is:
# 🔹 Removing all duplicates → the element is NOT predefined
# 🔹 Removing all occurrences → the element IS predefined

# (MEMORIZE THIS)
# 🔥 Whenever you pre-allocate an array, you MUST track how much you filled.(position-pos)

# You want to decide this:
# “Is arr[i] already inside new_arr[0 : pos]?”
# This question cannot be answered by one if because:
# new_arr has multiple values
# You must check them one by one
# The result is known only after the scan finishes
# So:
# if → works for one comparison
# loop → needed for searching
# Why if…else alone is impossible
# Because:
# new_arr is a list
# You’re not comparing one value
# You need to search through indexes
# So a loop is mandatory.
# ✅ What is possible:
# Loop + index check
# Loop + break + loop-else
# Loop + flag (you rejected this — good)
# ❌ What is NOT possible:
# Single if…else without looping

        # ⚠️ IMPORTANT: ANOTHER WAY IS This else is NOT normal if…else
        # This part: (not using another added bool flag)

        # for k in range(pos):
        #     if new_arr[k] == arr[i]:
        #         break
        # else:
        #     new_arr[pos] = arr[i]

        # Means:
        # “If the loop did not break, then run else.”
        # This is loop-else, not if-else.

# (Memorize this)
# 🔥 If a decision depends on searching multiple elements, a loop is mandatory.

# ---My Basic 1st try---
# arr = [3, 5, 3, 2, 5, 1, 5, 2]
# n= len(arr)
# new_arr = [0]*n

# for i in range(n):
#     for j in range(i+1,n):
#         if arr[i] == arr[j]:
#             new_arr[j] = arr[j]
#             break
        
# print(new_arr)