#insert an elemnt at the given porition
# Input: thelist[] = [10, 20, 30, 40], position = 3, element = 50
# Output: [10, 50, 20, 30, 40]

# Using Dynamic Position
#Position 3 (3rd Position) means 30 (In general), which means index 2. and from that others gonna be shifted.

thelist = [10,20,30,40]
element = 50
position = 3 #(3rd position)

n= len(thelist) #4
addedlist= thelist+[0]


for i in range (n-1,position-2,-1):
    addedlist[i+1] = addedlist[i]
    print(*addedlist)

addedlist[position-1]=element

print('\n','Insert 50 at the 3rd position (index 2):',*addedlist)