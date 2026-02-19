def reversestr(str):
    n=len(str)
    for i in range(n-1,-1,-1):
        print(str[i],end='')
        
word= 'YoBro'
reversestr(word)
