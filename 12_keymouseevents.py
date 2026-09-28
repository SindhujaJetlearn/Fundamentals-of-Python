import random
import turtle
sam = turtle.Turtle()
sam1= turtle.Turtle()
sam2= turtle.Turtle()
sam.shape("turtle")
sam1.shape("turtle")
sam2.shape("turtle")
screen = turtle.Screen()

sam.color("red")
sam1.write("Start", font = ("Courier",32, "bold"), align = ("right"))

x = int(input("enter the steps that you want for your turtle to move:"))

def go_forward():
  sam.forward(x)

def go_up():
  sam.setheading(90)

def go_down():
  sam.setheading(270)

def go_right():
  sam.setheading(0)

def go_left():
  sam.setheading(180)

def on_click(x,y):
  screen.tracer(0)
  sam.setheading(sam.towards(x,y))
  sam.goto(x,y)
  screen.tracer(1)
  print(sam.pos())
  if sam.pos==(100,30):
    sam.write("You win", font=("Courier",32,"bold"), align = ("right"))

def on_drag(x,y):
  screen.tracer(0)
  sam.goto(x,y)
  screen.tracer(1)

#Link the function with the key
screen.listen()
screen.onkey(go_forward,"space")
screen.onkey(go_left,"Left")
screen.onkey(go_up,"Up")
screen.onkey(go_down,"Down")
screen.onkey(go_right,"Right")

screen.onclick(on_click)
sam.ondrag(on_drag)


sam1.goto(100,30)

import random
for x in range(100):
  sam2.forward(100)
  sam2.right(36)
  sam2.backward(100)
  sam2.forward(100)
  sam2.forward(50)
  sam2.right(90)
  sam2.backward(20)
screen.mainloop()