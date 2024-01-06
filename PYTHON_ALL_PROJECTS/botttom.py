import top
n = top.n
# n = int(input("enter value: "))
for i in range(n):
    for j in range(i + 1):
        print(" ",end="")
    for j in range(i , n-1):
        print("*" ,end="")
    for j in range(i , n):
        print("*" ,end="")
    print()
