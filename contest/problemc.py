def removefromback(array):
    
    
    newbox=[0]* (len(array)-1) #
    
    i=0
    while i < (len(array)-1):
        newbox[i]=array[i]
        i=i+1
    
    return newbox
    
List=[1,2,3,4,5,6,6,5,7,8]
print(removefromback(List))

# import sys

# def solve():
#     input = sys.stdin.readline
#     T = int(input().strip())
#     for case in range(1, T + 1):
#         H = int(input().strip())
#         results = []
#         for d in range(10):
#             if H - d >= 0 and (H - d) % 9 == 0:
#                 k = (H - d) // 9
#                 A = 10 * k + d
#                 if A > 0:
#                     results.append(A)
#         results.sort()
#         print(f"Case {case}:", *results)

# if __name__ == "__main__":
#     solve()