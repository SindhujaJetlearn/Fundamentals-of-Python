"""
# define the function
def add():
  print(10+20)
  
#call the func
add()

#Function with parameters
def add(a,b): #parameters
  print(a+b)
  
add(10,70) #Arguments
add(80,90)

#return

def sub(a,b): #parameters
  return a-b
  
ans = sub(5,3)
print(ans)

print(sub(9,7))

sub(100,90)
  
"""

"""
#Define the function
def greet():
  print("Hi")
  
#call the function
greet()

#function with parameter
def welcome(name):
  print("Hi "+ name)
  
#Argument
welcome("Ayaansh")
welcome("Sindhuja")

"""

import turtle

t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor("sky blue")
t.speed(10)

def go(x,y):
  t.penup()
  t.goto(x,y)
  t.pendown()

def body(clr):
  t.color(clr)
  t.begin_fill()
  for i in range(4):
    t.forward(200)
    t.right(90)
  t.end_fill()

#call the function
go(0,0)
body("cadetblue")

def roof(clr):
  t.color(clr)
  t.begin_fill()
  for i in range(3):
    t.forward(200)
    t.left(120)
  t.end_fill()

roof("sienna")

def window(clr):
  t.color(clr)
  t.begin_fill()
  for i in range(4):
    t.forward(50)
    t.right(90)
  t.end_fill()

go(30,-50)
window("tan")

go(30,-125)
window("tan")

go(125,-50)
window("tan")

go(125,-125)
window("tan")

def grass(clr):
  t.color(clr)
  t.begin_fill()
  for i in range(3):
    t.forward(10)
    t.left(120)
  t.end_fill()
  

go(-100,-200)
for i in range(40):
  grass("olive")
  t.forward(10)


s.mainloop()














