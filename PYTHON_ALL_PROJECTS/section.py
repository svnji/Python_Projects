degrees = list(map(float, input().split()))
x = []
for i in degrees:
    if i >= 96:
        x.append(4)
    elif i >= 92:
        x.append(3.7)
    elif i >= 88:
        x.append(3.4)
    elif i >= 84:
        x.append(3.2)
    elif i >= 80:
        x.append(3)
    elif i >= 76:
        x.append(2.8)
    elif i >= 72:
        x.append(2.6)
    elif i >= 68:
        x.append(2.4)
    elif i >= 64:
        x.append(2.2)
    elif i >= 60:
        x.append(2)
    elif i >= 55:
        x.append(1.5)
    elif i >= 50:
        x.append(1)
    elif i < 50:
        x.append(0)
print(round(sum(x) / len(x), 2))
