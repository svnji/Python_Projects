chose = int(input("1- km to mile , 2- mile to km"))
if chose == 1:
    km = int(input("your value: "))
    result = km * 0.621
    print(result)
elif chose == 2:
    mile = int(input("your value: "))
    result = mile / 0.621
    print(result)
    