import turtle
import random   

screen = turtle.Screen()
screen.bgcolor("black")
t = turtle.Turtle() 
t.pensize(3)
t.speed(0)
screen.colormode(255)

for i in range(10):
  
  x = random.randint(-200,200)
  y = random.randint(-200,200)

  t.penup()
  t.goto(x,y)
  t.pendown()
  
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  t.color(r,g,b)
  
  for i in range(36) :
    s = random.randint(60,80)
    t.forward(s)
    t.backward(s)
    t.left(10)
 
 
 
screen.mainloop() 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 