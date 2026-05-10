from turtle import *
import random
width = 1000
height = 1000
setup(width, height)
yh = 100
xb = -265.5
yb = 0
yrand = [100, 75, 50, 25, 0, -25, -50, -75, -100]
pensize(15)

tracer(1000, 1)



penup()

goto(-300, 100)
setheading(0)
color('black')
pendown()
forward(600)

for i in range(5):
    goto(-300, yh)
    pendown()
    setheading(0)
    color('black')
    forward(600)
    penup()
    yh -= 50

for i in range(8):
    penup()
    setheading(0)
    yb = random.choice(yrand)
    goto(xb, yb)
    pendown()
    fillcolor("#318ce7")
    begin_fill()
    circle(25, 360)
    end_fill()
    xb += 75
    penup()
    forward(25)
    setheading(90)
    forward(25)
    pendown()
    forward(125)
    penup()
update()
done()

# This generative piece of art is inspired by musical notes, but filled out with colourful centers, to add a dash of artistic whimsy. It came to me as I realised I have been procrastinating my musical hobbies for too long. The random generation idea came to me when I was thinking about frameworks and possibilities for the integration of randomness within these frameworks.