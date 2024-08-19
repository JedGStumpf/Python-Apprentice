"""
Color Lines

1) Finish the program to make Tina draw a square with each side being a different color. 

"""

import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2)                           # Make the turtle move as fast, but not too fast. 


colors = [ 'red', 'blue', 'black', 'orange']    # define a list of colors

for color in colors:                            # loop through the colors
    tina.forward(100)
    tina.color(color)
    tina.right(90)

# 2) Make another square, but put the colors in reverse order, using a negative index. 
tina.goto(25, 150)
 # Your code here
for color in colors[::-1]:
    tina.forward(50)
    tina.color(color)
    tina.right(90)

turtle.done()