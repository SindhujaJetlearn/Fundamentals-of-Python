import turtle
import random
import time

# Create screen
screen = turtle.Screen()
screen.setup(width=500, height=400)  # Set the screen size in Trinket
screen.bgcolor("pink")


#Finish line
t=turtle.Turtle()
t.pensize(10)
t.color("black")
t.penup()
t.goto(200,200)
t.pendown()
t.right(90)
t.forward(400)   

# Small delay to allow screen to initialize properly
time.sleep(0.5)

# Create user turtle
user = turtle.Turtle()
user.shape("turtle")
user.color("red")
user.penup()
user.goto(-200, 100)

# Function to move the user turtle
def move_right():
    x = user.xcor()
    if x < 200:
        user.setx(x + 20)

# Keyboard event for moving the user turtle
screen.listen()
screen.onkey(move_right, "Right")

# Create players
colors = ["blue", "green", "orange", "purple"]
players = []

# Set initial Y position for players
y_pos = -100

# Position and create players, store each player's color
for color in colors:
    player = turtle.Turtle()
    player.shape("turtle")
    player.color(color)
    player.penup()
    player.goto(-200, y_pos)
    players.append((player, color))  # Store tuple of (turtle object, color)
    y_pos += 50

# Move players forward
def move_players():
    for player, color in players:
        speed = random.randint(1, 10)
        player.forward(speed)

# Game loop
game_over = False
winner = None  # Track the winner's color

while not game_over:
  move_players()
  for player, color in players:
    if player.xcor() >= 195:
      game_over = True
      if user.xcor() > player.xcor():
        winner = "red"
      else:
        winner = color  # Retrieve color directly from tuple
      break
# Display the winner
if winner:
    turtle.penup()
    turtle.hideturtle()
    turtle.goto(0, 0)
    turtle.write("The {} turtle wins!".format(winner.upper()), align="center", font=("Arial", 16, "bold"))

screen.mainloop()




































