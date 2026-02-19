def palindrome(txt):
    left = 0 
    right= len(txt)-1 
    
    while left<right:
        if txt[left]!=txt[right]:
            return False
        left = left+1
        right = right-1
    return True

word='asdasd'
print(palindrome(word))