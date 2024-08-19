"""
Copy the code from the previous lesson, 08a_More_Turtle_programs.ipynb, 
from the section " Click on the Turtle"

Then change the code so that the turtle has a different image ( look in the 'images'
directory ) and when you click on it, it moves to a random location on the screen.

Use this code to get a random x and y location


    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)

"""
# Click on the Turtle


import turtle as turtle

turtle.setup(width=600, height=600)

t = turtle.Turtle()

t.shape("turtle")
t.turtlesize(stretch_wid=10, stretch_len=10, outline=4) # Make the turtle really big

def turtle_clicked(t, x, y):
    """Function that gets called when the user clicks on the turtle

    This function will make the turtle tilt 20 degrees 18 times, making a full
    circle. It is called by the turtle when the user clicks on it.

    Args:
        t (Turtle): The turtle object that was clicked
        x (int): The x coordinate of the click
        y (int): The y coordinate of the click
    """

    print('turtle clicked!')
    
    for i in range(0,360, 20): # Full circle, 20 degrees at a time
        t.tilt(20) # Tilt the turtle 20 degrees

# Connect the turtle to the turtle_clicked function
t.onclick(lambda x, y, t=t: turtle_clicked(t, x, y))


turtle.done() # Important! Use `done` not `exitonclick` to keep the window open
# ```

# In the line `t.onclick(lambda x, y, t=t: turtle_clicked(t, x, y))` the
# lambda keyword is used to create an anonymous function, a function that does not
# have a name.  Lambda functions are advanced, we'll explain them in a future
# lesson,  but for now, just know that this is a way to pass arguments to a
# function when using the `onclick` method. You can just copy this line to make
# the turtle respond to clicks.


## But Which Turtle?
# Unfortunately, if you have multiple turtles, you wont be able to tell which
# turtle was clicked on in the ``turtle_clicked`` function. Here is one way to
# solve that problem, using some advanced Python that we have not learned yet. 


# ```python
import turtle as turtle

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')

t = turtle.Turtle()
t.penup()
t.shape("turtle")
t.turtlesize(stretch_wid=10, stretch_len=10, outline=4)

def turtle_clicked(t, x, y):

    print('turtle clicked!')
    
    for i in range(0,360, 20):
        t.tilt(20)

t.onclick(lambda x, y, t=t: turtle_clicked(t, x, y))

turtle.done() # Important! Use `done` not `exitonclick` to keep the window open
# ```