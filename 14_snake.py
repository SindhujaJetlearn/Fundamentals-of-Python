import turtle
import time
import random

sc = turtle.Screen()
sc.bgcolor("cadetblue")

#snake
snake = turtle.Turtle()
snake.shape("square")
snake.color("black")
snake.penup()
snake.goto(0, 100)
snake.direction = "stop"

#food turtle
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(100, 100)

score = 0

#Pen turtle
pen = turtle.Turtle()
pen.color("green")
pen.penup()
pen.goto(100, 150)
pen.write("Score: {}".format(score), align="center", font=("Arial", 20, "normal"))
pen.hideturtle()

#Move snake
def move():
  if snake.direction == "Up":
    y = snake.ycor()
    snake.sety(y + 20)
  if snake.direction == "Down":
    y = snake.ycor()
    snake.sety(y - 20)
  if snake.direction == "Right":
    x = snake.xcor()
    snake.setx(x + 20)
  if snake.direction == "Left":
    x = snake.xcor()
    snake.setx(x - 20)


#Setting up directions
def go_up():
  snake.direction = "Up"


def go_down():
  snake.direction = "Down"


def go_left():
  snake.direction = "Left"


def go_right():
  snake.direction = "Right"


#link with functions
sc.listen()
sc.onkey(go_up, "Up")
sc.onkey(go_down, "Down")
sc.onkey(go_right, "Right")
sc.onkey(go_left, "Left")


segments = []  #new segement of snake will be saved


#infinite
while True:
  sc.update()
  move()
  time.sleep(0.1)
  if snake.distance(food) < 20:
    x=random.randint(-180,180)
    y=random.randint(-180,180)
    food.goto(x,y)

    score=score+10
    pen.clear()
    pen.write("Score : {}".format(score), align="center", font=("Arial", 20, "normal"))

    new_s=turtle.Turtle()
    new_s.shape('square')
    new_s.color('gray')
    new_s.penup()
    segments.append(new_s)

  #len(segments)-1 - gives index of last element(reverse looping)
  for i in range(len(segments) - 1, 0, -1):
    #New segment gets added to the last segment of the snake
    x = segments[i - 1].xcor()
    y = segments[i - 1].ycor()
    segments[i].goto(x, y)

  #If only one segement exists - attach it to head of snake
  if len(segments) > 0:
    x = snake.xcor()
    y = snake.ycor()
    segments[0].goto(x, y)

sc.mainloop()








