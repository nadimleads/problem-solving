# Insert an elemnt at the given porition
# Input: thelist[] = [10, 20, 30, 40], position = 3, element = 50
# Output: [10, 50, 20, 30, 40]



# Using Dynamic Position
#Position 3 (3rd Position) means 30 (In general), which means index 2. and from that others gonna be shifted.
thelist = [10, 20, 30, 40]
element = 50
position = 3   # means insert at any position (index = position-1 = 2)

n = len(thelist)
addedlist = thelist + [0]

# Check for valid position input
if position <= 0 or position > n + 1:
    print("Invalid Input")
else:
    for i in range(n - 1, position - 2, -1):
        addedlist[i + 1] = addedlist[i]

    addedlist[position - 1] = element

    print('inserted 50 at given position-',*addedlist)