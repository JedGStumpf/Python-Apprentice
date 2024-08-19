""" Leaguebot

Write your own turtle program! Here is what your program should do

1) Change the turtle image to 'leaguebot_bolt.gif'
2) Change the turtle size to 10x10
3) Change the turtle line color to 'blue'
4) Draw a hexagon using a loop and variables. 

"""

import turtle as turtle
from pathlib import Path


screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')

t = turtle.Turtle()
t.turtlesize(10, 10, 4)
t.pencolor("blue")
# Your Code Here
def set_turtle_image(turtle, image_name):
    """Set the turtle's shape to a custom image."""

    
    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)

    screen = turtle.getscreen()
    screen.addshape(image_path)
    turtle.shape(image_path)





set_turtle_image(t, 'leaguebot_bolt.gif')

def draw_poly(sides, side_len):
    for _ in range(sides):
        t.forward(side_len)
        t.right(360/sides)

draw_poly(5, 100)

turtle.done()