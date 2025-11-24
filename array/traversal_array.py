#traverse an array

arr= [2,3,4,5,6,7]
n= len(arr) #6 (0-5)

for i in range (0,n,1):
    if (arr[i]== arr[n-1]):
        print(arr[i],end='')
    else:
        print(arr[i],end=',')