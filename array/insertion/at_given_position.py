#ALHAMDULILLAH MASHAALLAH SUBHANALLAH

#insert an elemnt at the given porition
# Input: arr[] = [10, 20, 30, 40], 
# in position 2 insert elemnet = 50
# Output: [10, 20, 50, 30, 40]

# it runs for i = 3, 2, but not correctly adjusted if the insertion position changes — it’s hardcoded.

thelist = [10,20,30,40]
element = 50

n= len(thelist) #4
addedlist= thelist+[0]
print (addedlist) #[10,20,30,40,0]

for i in range (n-1,1,-1):
    addedlist[i+1] = addedlist[i]

addedlist[2]=element

print('\n','Insert 50 at the position 2:',*addedlist)