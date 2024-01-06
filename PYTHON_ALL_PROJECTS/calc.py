from tkinter import *
import tkinter.messagebox
import math
root = Tk()
root.geometry("650x400+300+300")
root.title("calculator")
switch = None
#calculator
def calc():
     op = input(" + , - , * , / ")
     if op == "+":
          num1 = int(input("num1: "))
          num2 = int(input("num2: "))
          result = num1 + num2
          print(result)
     elif op == "-":
          num1 = int(input("num1: "))
          num2 = int(input("num2: "))
          result = num1 - num2
          print(result)
     elif op == "*":
          num1 = int(input("num1: "))
          num2 = int(input("num2: "))
          result = num1 * num2
          print(result)
     elif op == "/":
          num1 = int(input("num1: "))
          num2 = int(input("num2: "))
          result = num1 / num2
          print(result)
     print("(;")
calc()
root.mainloop()