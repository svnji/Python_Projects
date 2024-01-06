
def calc():
      size = input("The Gamee Size By (GB) : ")
      speed = input("The Internet Speed (MBPS) : ")
      speed1 = float(speed) * 0.125
      A = float(size) * 1024
      B = float(A) / speed1
      C = float(B) / 60

      print("Its Will Take " + str(C) + " Minutes To Download")

calc()

again = input("Again? ")
if again.lower() == "yes":
      calc()
      again = input("Again? ")

elif again.lower() == "no":
      exit("thank you")
else:
      print("eror")
