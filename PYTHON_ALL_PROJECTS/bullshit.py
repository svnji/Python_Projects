# number of students
n = int(input("enter the num of studens: "))  # num of studens

grades = []

for i in range(n):
    grades.append(float(input("enter student's grade: ")))

x = 0  # (2:2.49)
y = 0  # (2.5:2.99)
z = 0  # (3:3.49)
w = 0  # (3.5:4)

for grade in grades:
    if 2 <= grade < 2.5:
        x += 1
    elif 2.5 <= grade < 3:
        y += 1
    elif 3 <= grade < 3.5:
        z += 1
    elif 3.5 <= grade < 4:
        w += 1

print(x)
print(y)
print(z)
print(w)

print(" the percentage of students (2:2.49): ", (x / n) * 100, '%')
print(" the percentage of students (2.5:2.99): ", (y / n) * 100, '%')
print(" the percentage of students (3:3.49): ", (z / n) * 100, '%')
print(" the percentage of students (3.5:4): ", (w / n) * 100, '%')
