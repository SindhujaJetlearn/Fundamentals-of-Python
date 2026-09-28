import turtle

t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor("pink")
t.speed(0)
t.fillcolor("white")

#Base of snowman
t.begin_fill()
for i in range(36):
  t.forward(16)
  t.right(10)
t.end_fill()

#Body of snowman
t.begin_fill()
for i in range(36):
  t.forward(12)
  t.left(10)
t.end_fill()

#Eyes of snowman
t.penup()
t.goto(-20,90)
t.pendown()
t.dot(10)

t.penup()
t.goto(20,90)
t.pendown()
t.dot(10)

#smile
t.penup()
t.goto(-25,60)
t.pendown()
t.right(90)

for i in range(19):
  t.forward(5)
  t.left(10)
  

t.hideturtle()
s.mainloop()

"""
import turtle

pen=turtle.Turtle()
paper=turtle.Screen()

paper.bgcolor("blue")
pen.speed(0)

pen.fillcolor("white")

pen.begin_fill()
pen.circle(50)
pen.end_fill()

pen.penup()
pen.goto(0,-140)
pen.pendown()
pen.circle(70)

paper.mainloop()
"""
