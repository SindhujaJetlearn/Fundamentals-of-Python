"""
#define the function
def greet():
  print("Hi I am Yusuf")
  
#Call the function
greet()

#function with parameter
def greet(name):
  print("Hi I am "+name)
  
#Call the function with argument
greet("Sindhu")
greet("Yusuf")
greet("Remi")

"""


import turtle
pen=turtle.Turtle()
paper=turtle.Screen()

paper.setup(600,500)
paper.bgcolor("sky blue")
pen.speed(0)

#create user defined function
def move(x,y):
  pen.penup()
  pen.goto(x,y)
  pen.pendown()

#Sun
#Call the function
move(180,180)
pen.color("yellow")

pen.begin_fill()
for i in range(4):
  pen.forward(80)
  pen.right(90)
pen.end_fill()

move(220,200)
pen.right(45)

pen.begin_fill()
for i in range(4):
  pen.forward(80)
  pen.right(90)
pen.end_fill()

pen.left(45)

#Pyramid
pen.color("goldenrod")
move(-100,-100)

pen.begin_fill()
for i in range(3):
  pen.forward(240)
  pen.left(120)
pen.end_fill()

#sand
move(-300,-100)

pen.color("tan")
pen.begin_fill()
for i in range(2):
  pen.forward(600)
  pen.right(90)
  pen.forward(200)
  pen.right(90)
pen.end_fill()

#Striped lines
pen.color("orange")
pen.pensize(5)

move(-10,60)
pen.forward(60)

move(-40,10)
pen.forward(120)

move(-70,-40)
pen.forward(180)

paper.mainloop()
