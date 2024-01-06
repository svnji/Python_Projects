m = int(input('ha: '))
fact = 1
for i in range(1, m + 1):
    if fact == 0:
        print(1)

    fact *= i
print(fact)

#
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


num = int(input('enter ur value: '))
print("Factorial of", num, "is", factorial(num))
