# Rotate an Array (Experiment Version- insertion + deletion manually)

def rotate_array(array):
    
    # insertion (modified)
    n = len(array)
    new_array= array +[0] # Increase size of array

    for i in range (n-1,-1,-1):
        new_array[i+1] = new_array[i]

    print('extended array for check:',new_array)

    # deletion (modified)
    nx= len(new_array)-1
    new_array[0]= new_array[nx]
    print('modified array for check:',new_array)
    rotated_array = [0]*nx # taking another same size empty array

    for x in range (nx):
        rotated_array[x] = new_array[x] #assign in the another array (not using loop printing from deletion)

    return rotated_array

array =[10,20,30,40]
result= rotate_array(array)
print('Rotated array:',*result) # making it array style


    #---------My learnign understanding part----------
# [1,2,3,4] to [4,2,3,1]
# Here:
# 4 jumped to front ✅
# but 1 jumped to back ❌
# middle order stayed same accidentally
# ➡️ This breaks order
# ➡️ So it is NOT rotatio

# So, 
# Rotation means shifting elements of an array either:
#     Move elements to the left, and the first element goes to the end.
#     or,
#     Move elements to the right, and the last element comes to the front.
    
# ---NOT ROTATION IS---
# Swap first & last
# Reverse	
# Shuffle