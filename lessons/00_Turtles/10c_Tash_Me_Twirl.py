
""" Tash Me with a Twirl
 
Update your Tash Me Click program ( copy your old program here )
so the moustache will twirl when you click on it. 

Hint: See 08a_More Turtle Programs, section 'Click on the Turtle'
"""

# Your code here

import turtle as turtle
from pathlib import Path


screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')

t = turtle.Turtle()
t.shape('turtle')
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



def screen_clicked(x, y):
    """Print the x and y coordinates of the screen when clicked.
    and make the turtle move to the clicked location."""

    print('You pressed: x=' + str(x) + ', y=' + str(y))

    t.goto(x, y)


def turtle_clicked(t, x, y):

    print('turtle clicked!')
    
    for i in range(0,360, 20):
        t.tilt(20)


screen = turtle.Screen()
set_background_image(screen, "emoji.png")
# set_turtle_image(t, 'moustache1.gif')
# screen.onclick(screen_clicked)
t.onclick(lambda x, y, t=t: turtle_clicked(t, x, y))
turtle.done() 
