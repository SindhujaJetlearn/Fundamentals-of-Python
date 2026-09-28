import turtle

paper = turtle.Screen()
pen = turtle.Turtle()

pen.write("Press R to turn your bgcolor red, G to turn it green and B to turn it blue", font=("Arial", 8), align="center")

def red():
  paper.bgcolor("red")
  
def green():
  paper.bgcolor("green")
  
def blue():
  paper.bgcolor("blue")
  
paper.listen()

paper.onkey(red, "r")
paper.onkey(green, "g")
paper.onkey(blue, "b")

pen.hideturtle()
paper.mainloop()