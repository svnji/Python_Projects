n = int(input("Number of rows: "))
for i in range(n - 1):
    for j in range(i , n):
        print(" ",end="")
    for j in range(i):
        print("*" ,end="")
    for j in range(i +1):
        print("*" ,end="")
    print()
