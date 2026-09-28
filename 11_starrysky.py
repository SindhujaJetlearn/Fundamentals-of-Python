import turtle
import random
t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("indigo")
t.pensize(3)
t.speed(40)
screen.colormode(255)

for i in range(15):
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  t.pencolor(r,g,b)
  t.fillcolor(r,g,b)
  x = random.randint(-200,200)
  y = random.randint(-200,200)
  t.penup()
  t.goto(x,y)
  t.pendown()

  count = 0
  t.begin_fill()
  d = random.randint(10,100)
  while(count<6):
   t.forward(d)
   t.left(144)
   count = count+1
  t.end_fill()
  t.right(45)
  
screen.mainloop()
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  