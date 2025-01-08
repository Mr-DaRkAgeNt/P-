import turtle#For Animation Window
import time#For game Time
import random#For Using Random coordinates in a plane

delay = 0.1
score = 0
high_score = 0

# Setting up the window for the game
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("orange")
wn.setup(width=600, height=600)
wn.tracer(0)  # Turns off the screen when it updates

#Making The head of Snake
h = turtle.Turtle()
h.speed(0)
h.shape("triangle")
h.color("white")
h.penup()
h.goto(0, 0)
h.direction = "stop"

# Snake food Architect
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("white")
food.penup()
food.goto(0, 100)#GOTO function Helps in positioning The food in a game's plane

segments = [] #Using Empty List for storing the Snake body components

#  Object For Motion and Animation In Game
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

#Making The Motion Functions
def go_up():
    if h.direction != "down":
        h.direction = "up"

def go_down():
    if h.direction != "up":
        h.direction = "down"

def go_left():
    if h.direction != "right":
        h.direction = "left"

def go_right():
    if h.direction != "left":
        h.direction = "right"

def move():
    if h.direction == "up":
        y = h.ycor()
        h.sety(y + 20)

    if h.direction == "down":
        y = h.ycor()
        h.sety(y - 20)

    if h.direction == "left":
        x = h.xcor()
        h.setx(x - 20)

    if h.direction == "right":
        x = h.xcor()
        h.setx(x + 20)

# Assigning The Keyboard Keys For The Movement Functions
wn.listen()
wn.onkey(go_up, "w")
wn.onkey(go_down, "s")
wn.onkey(go_left, "a")
wn.onkey(go_right, "d")

# Main game loop
while True: #Creation of Infinite Loop For Running The Game Until The Player loses
    wn.update()

    # Checking a collision of the head with Borders of the Terminal
    if h.xcor() > 290 or h.xcor() < -290 or h.ycor() > 290 or h.ycor() < -290:
        time.sleep(1)
        h.goto(0, 0)
        h.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()

        # Reset the score
        score = 0

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Check for a collision with the food
    if h.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score += 10

        if score > high_score:
            high_score = score #Basic Game Logic

        pen.clear()#Checks if the head eats the food and updates the score, food position, and snake length.
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Move the end segments first in reverse order To follow the Head
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = h.xcor()
        y = h.ycor()
        segments[0].goto(x, y)

    move()

    # Check for head collision with body components
    for segment in segments:
        if segment.distance(h) < 20:
            time.sleep(1)
            h.goto(0, 0)
            h.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()

            # Reset the score
            score = 0

            pen.clear()#Object Loop calling
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)#Controlling The speed of the game

wn.mainloop()

