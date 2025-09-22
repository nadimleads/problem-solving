# Using while loop for the shifting to the right logic

array= [10,20,30,40]
    #    0  1  2  3
item=100
length= len(array) #4

new_array= array+[0] #[10,20,30,40,0]


i = length-1 #4-1 = 3

while (i>=0): #3, 2, 1, 0, -2
    new_array[i+1] = new_array[i]
    i -= 1
    print(*new_array)

new_array[0] = item

print('\nAfter insert: ', *new_array)

print('Insert(traverse using while:')
n= 0
x = len(new_array)-1
while(n<=x):
    print (new_array[n],end=' ')
    n += 1