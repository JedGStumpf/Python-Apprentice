""" Tash Me

Write a program that:
1) Loads an emoji image as the background
2) Make the turtle shape a moustach
3) Move the moustache to the right spont on the emoji

Hint: See 08a_More Turtle Programs, section 'Change the Background Image' and
'Change the Turtle Shape'
"""

... # Your code here

import turtle as turtle
from pathlib import Path


screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')

t = turtle.Turtle()
t.turtlesize(10, 10, 4)
t.penup()
# Your Code Here
def set_turtle_image(turtle, image_name):
    """Set the turtle's shape to a custom image."""

    
    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)

    screen = turtle.getscreen()
    screen.addshape(image_path)
    turtle.shape(image_path)

# Change the Background Image
def set_background_image(window, image_name):
    """Set the background image of the turtle window to the image with the given name."""

    from pathlib import Path
    from PIL import Image


    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)

    image = Image.open(image_path)
    
    window.setup(image.width, image.height, startx=0, starty=0)
    window.bgpic(image_path)



screen = turtle.Screen()
set_background_image(screen, "emoji.png")
set_turtle_image(t, 'moustache1.gif')

def screen_clicked(x, y):
    """Print the x and y coordinates of the screen when clicked.
    and make the turtle move to the clicked location."""

    print('You pressed: x=' + str(x) + ', y=' + str(y))

    # t.goto(x, y)
  
screen.onclick(screen_clicked)

turtle.done() 

