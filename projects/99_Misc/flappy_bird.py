import turtle
import random
import time

# Setup the screen
win = turtle.Screen()
win.title("Flappy Bird")
win.bgcolor("sky blue")
win.setup(width=500, height=600)
win.tracer(0)

# Variables
gravity = -0.4
flap_strength = 10
pipe_speed = -3
pipe_gap = 200
score = 0

# Bird setup
bird = turtle.Turtle()
bird.shape("circle")
bird.color("yellow")
bird.penup()
bird.goto(-100, 0)
bird.dy = 0  # Vertical speed

# Pipe setup
pipes = []
pipe_width = 40

# Score display
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(0, 250)
score_display.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

# Functions
def flap():
    bird.dy = flap_strength

def create_pipe():
    top_pipe = turtle.Turtle()
    top_pipe.shape("square")
    top_pipe.color("green")
    top_pipe.shapesize(stretch_wid=18, stretch_len=2)
    top_pipe.penup()
    top_pipe.goto(250, random.randint(100, 300))
    pipes.append(top_pipe)
    
    bottom_pipe = turtle.Turtle()
    bottom_pipe.shape("square")
    bottom_pipe.color("green")
    bottom_pipe.shapesize(stretch_wid=18, stretch_len=2)
    bottom_pipe.penup()
    bottom_pipe.goto(250, top_pipe.ycor() - pipe_gap - 360)
    pipes.append(bottom_pipe)

def update_score():
    global score
    score += 1
    score_display.clear()
    score_display.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

def reset_game():
    global score, pipes
    time.sleep(1)
    bird.goto(-100, 0)
    bird.dy = 0
    score = 0
    score_display.clear()
    score_display.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))
    
    for pipe in pipes:
        pipe.hideturtle()
    pipes = []

# Keyboard binding
win.listen()
win.onkeypress(flap, "space")

# Main game loop
while True:
    win.update()
    
    # Bird gravity
    bird.dy += gravity
    bird.sety(bird.ycor() + bird.dy)
    
    # Bird boundaries
    if bird.ycor() < -290 or bird.ycor() > 290:
        reset_game()
    
    # Pipe management
    if len(pipes) < 4 or pipes[-1].xcor() < 100:
        create_pipe()
    
    for pipe in pipes:
        pipe.setx(pipe.xcor() + pipe_speed)
        
        # Check for collision with bird
        if pipe.distance(bird) < 20:
            reset_game()
        
        # Remove pipes and update score
        if pipe.xcor() < -250:
            pipe.hideturtle()
            pipes.remove(pipe)
            if pipe.ycor() > 0:  # Only increment score once per pair of pipes
                update_score()
    
    # Delay to control game speed
    time.sleep(0.02)
