from turtle import *
import random

width = 1000
height = 1000
setup(width, height)
xb = -265.5
pensize(15)
tracer(1000, 1)
# These are the parameters for the canvas on which the program will draw using turtle.

def note():
    pendown()
    fillcolor("#318ce7")
    begin_fill()
    circle(25, 360)
    end_fill()
    penup()
    forward(25)
    setheading(90)
    forward(25)
    pendown()
    forward(125)
    penup()
# This piece of code defines the function that the program uses to create a note on turtle.
def get_next_y(prev_y):
    yrand = [100, 75, 50, 25, 0, -25, -50, -75, -100]
    available_y = [y for y in yrand if y != prev_y]
    return random.choice(available_y)
# Here, the function is defined that selects a random y-coordinate from the list yrand. The function checks if the previous circle (note) was drawn on one of the variables included in yrand and if it was, draws the next note on a different random variable included in yrand.
def randomise(prev_y):
    yb = get_next_y(prev_y)
    penup()
    setheading(0)
    goto(xb, yb)
    return yb
# This function randomises which of the variables in yrand is chosen.
def framework():
    penup()
    goto(-300, 100)
    setheading(0)
    color('black')
    pendown()
    forward(600)
    penup()
    yh = 50
    for i in range(4):
        goto(-300, yh)
        pendown()
        forward(600)
        penup()
        yh -= 50
# def framework() includes all of the instructions that turtle needs to draw the five lines necessary for the drawing to make sense, i.e. the guiding lines for the notes.

# This is where the main loop begins.
framework()

yrand = [100, 75, 50, 25, 0, -25, -50, -75, -100]
prev_y = random.choice(yrand)

for i in range(8):
    prev_y = randomise(prev_y)
    note()
    xb += 75

update()
done()