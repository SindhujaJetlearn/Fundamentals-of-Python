"""
#Variable - store values
name="Ayaansh"

#datatypes
#String
a="200"
b="hi"

#float - decimal number
c=6.3

#Integer
d=100

#Boolean
e=True
f=False

#questions - input()
color1=input("Enter the background color : ")
#print message, value - print()
print("The background color is "+color1) 

#Loop 
#for - know the num of repetition
#while - until a condition is satisfied, infinte loop

#1 less than last value
#range(start,end)
for num in range(1,11): 
  print(num)
  
print("---------------------")
#range(start, end, step)
for num in range(0,101,5): 
  print(num)
  
print("---------------------")
#while loop
num=10
while num <= 20:
  print(num)
  num+=1

print("---------------------")
num=10
while num >0:
  print(num)
  num-=1

print("---------------------")
for num in range(10,0,-1):
  print(num)

"""

#Star Pattern

import turtle

#pen
pen=turtle.Turtle()
#paper
paper=turtle.Screen()

#input() - asks questions
color1=input('Enter the Background color : ')

print(color1)
paper.bgcolor(color1)

color2=input('Enter the Pen color : ')
pen.color(color2)
print(color2)

pen.pensize(5)
pen.speed(0)

for i in range (20):
  pen.forward(150)
  pen.right(190)

pen.penup()
pen.goto(-50,0)
pen.pendown()

count=0
while count <= 20:
  pen.forward(150)
  pen.right(190)
  count = count + 1
  
paper.mainloop()


