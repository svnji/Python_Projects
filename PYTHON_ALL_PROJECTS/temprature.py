#temprature
temprature = int(input("enter your temprature: "))
if temprature > 30:
    print("very hot")
elif temprature >= 25 < 30:
    print("hot")
elif temprature >= 20 < 25:
    print("warm")
elif temprature >= 10 < 20:
    print("cold")
elif temprature > 0 < 10:
    print("very cold")
elif temprature <= 0:
    print("frozen")