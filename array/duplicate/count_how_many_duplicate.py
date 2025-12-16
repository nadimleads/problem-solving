# Count how many distinct elements appear more than once.

def find_distinct(arr):
    n=len(arr)
    arr_new=[0]*n
    position=0
    
    for i in range(n-1):
        for j in range(i+1,n):
            if arr[i]==arr[j]:
                for k in range(position):
                    if arr_new[k] == arr[i]:
                        break #do nothing 
                else:
                    arr_new[position]=arr[i]
                    position = position+1
    if position>0:
        return 'There are:',position, 'duplicate items'
    else:
        return 'There is no duplicate!', 'so total item is:', n

# arr = [3, 5, 3, 2, 5, 1, 5, 2]
arr = [3, 5, 2, 2, 1]
outupt=find_distinct(arr)

print(outupt)


# ---------My learnign understanding part----------

# My Q1. when the 1st i loop gonna take the last element of the array and 2nd (j) loop gonna start comparing, that time j is already i+1 means if i=7 then j=8 which is already = n...so why there is no index error as j hits 8 and, 

# My Q2. isnt shouldnt we make the code like that, so that i dosent even go to the very last element (as comparing all element is already done!?)
    
# Q1 Answer (short):
# No index error because range(i+1, n) becomes empty when i = n-1
# Python never accesses arr[j]

# Q2 Answer (short):
# Yes, i should ideally go to n-2
# Use range(n-1) for clean and optimized logic



# ---if then else outside of if and also outside loop---

# if–else inside loop means:
# “For EACH comparison, if this one isn’t equal → insert.” not wat we want❌

# But what you actually want is:
# “Only insert after checking ALL elements.”

    # so One-line golden rule 🧠
    # If the decision depends on “not found anywhere”, NEVER put else inside the loop.

# Adding else inside loop is like:
# First student is not Rahim
# So you add Rahim to the list immediately ❌

# Correct way:
# Check all students
# If Rahim is not found anywhere
# Then add Rahim ✔