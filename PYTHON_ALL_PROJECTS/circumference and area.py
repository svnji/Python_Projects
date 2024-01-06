#circumference and area
pi = 3.14
kind = input("circle or square or rectangle or tringle? ")
if kind.lower() == ("circle"):
    r = float(input("enter r: "))
    carea = pi * r**2
    ccircumference = 2 * pi * r
    print("area is: " ,carea)
    print("circumference is: " ,ccircumference)
elif kind.lower() == ("square"):
        l = float(input("enter r: "))
        sarea = l * l
        scircumference = l * 4
        print("area is: " ,sarea)
        print("circumference is: " ,scircumference) 
elif kind.lower() == ("rectangle"):
    x = float((input("enter x: ")))
    y = float(input("enter y: "))
    rarea = x * y
    rcircumference = (x + y) * 2
    print("area is: " ,rarea)
    print("circumference is: " ,rcircumference)
elif kind.lower() == ("tringle"):
    bottom = float(input("enter bottom: "))
    hight = float(input("enter hight: "))
    u = float(input("enter z: "))
    tcircumference = bottom + hight + u
    tarea = 0.5 * bottom * hight
    print("the area is: " ,tarea)
    print("the circumference is: " ,tcircumference)
else:
    print("eror")
print("(;")