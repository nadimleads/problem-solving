# Insert an elemnt at the end
# Input: thelistarr[] = [10, 20, 30, 40], ele = 50
# Output: [10, 20, 30, 40, 50]

thelist = [10,20,30,40]
ele = 50
n= len(thelist) #4
addedlist= thelist+[0]
print (addedlist) #[10,20,30,40,0]

addedlist[n]=ele

print('\n','Insert 50 at the end:',*addedlist)