"""
#Comparison Operators - >, < ,>= ,<= , == , !=
a=10
b=5
print(a==b) #check if both values are same
print(a!=b) #not equal
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

#Logical operators - and, or , not
#and - all the condition has to be true
#or - atleast 1 condition has to be true
print("not operator :",not True)
print("not operator :",not False)

age= int(input("Enter your age : "))
if (age > 18):
  print("You are an adult")
else:
  print("Your are not an adult")
  
math=95
sci=80
#and
if math>=90 and sci >=90:
  print("Buy chips")
else:
  print("No chips")

#or
if math>=90 or sci >=90:
  print("Buy chips")
else:
  print("No chips")
  
"""
import turtle
pen = turtle.Turtle()
paper=turtle.Screen()

shape = input("What do you want to be displayed ? \n1. circle \n2. triangle \n3. square \n")
if shape =="circle":
  print(" You chose circle!")
  pen.circle(50)
elif shape =="square":
  print("You chose square!:)")
  for i in range(4):
    pen.forward(100)
    pen.right(90)
elif shape =="triangle": 
  print("you chose triangle")
  for i in range(3):
    pen.forward(100)
    pen.left(120)     
else: 
  print ("put in circle,triangle or square not any other shape >:(")

paper.mainloop()