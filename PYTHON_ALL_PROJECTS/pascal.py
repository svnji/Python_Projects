from math import factorial

n = int(input("enter rows:"))

#main for loop
for i in range(n+1):
    #spaces
    for j in range(n-i+1):
        print(end=" ")
        #for loop for nums values
    for k in range(i+1):
        ele = factorial(i)/(factorial(k)*factorial(i-k))
        print(int(ele), end=" ")
    #new line
    print()