# Delete any duplicate item of an array (keep only those elements that occur exactly once)
# arr = [1,2,3,4,1,2]
# output arr=[3,4]






# ---------My learnign understanding part----------
# Another way

# def count_occurrence(arr, target):
#     count = 0
#     i = 0

#     while i < len(arr):
#         if arr[i] == target:
#             count = count + 1
#         i = i + 1

#     return count

# def remove_all_duplicates(arr):
#     n = len(arr)
#     result = [0] * n   # fixed size memory
#     result_index = 0

#     i = 0
#     while i < n:
#         current = arr[i]
#         occurrences = count_occurrence(arr, current)

#         if occurrences == 1:
#             result[result_index] = current
#             result_index = result_index + 1

#         i = i + 1

#     # trim unused part manually
#     final_result = [0] * result_index
#     j = 0
#     while j < result_index:
#         final_result[j] = result[j]
#         j = j + 1

#     return final_result

# arr = [1, 2, 3, 4, 1, 2]
# output = remove_all_duplicates(arr)
# print(output)
