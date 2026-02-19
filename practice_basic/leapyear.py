def leapyear(x):
    if (x %4 ==0 or x%400 == 0 and x %100 != 0):
        print (True)
    else:
        print(False)

year=2024
leapyear(year)