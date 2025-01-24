"""Fizzbuzz Grid

We're going to use a Windowing library, guizero, to create a 10x10 grid of
numbers, with each number in a separate cell, but we're also going to set the
color of the number based on the following rules:

* If the number is evenly divisible by 5, print '🦡'
* If the number is evenly divisible by 3, print '🍄'
* If the number is evenly divisible by 15, print '🐍'
* If it is divisible by neither, print the number.

Additionally, If you are displaying a number  color the numbers as follows:

* If the sum of the digits of the number is even, color the number blue
* If the sum of the digits of the number is odd, color the number red

Here is how you can display a number in your grid:

    Text(app, text=str(number), grid=[col, row], color=color)

Or to display a badger: 
    
    Text(app, text='🦡', grid=[col, row], color=color)

HINT: You can use % and // to get the first and last digit of a number, 
our you can convert the number to a string and iterate over the digits

"""
# from guizero import App, Box, Text

# app = App("Numbers Grid", layout="grid")

# Create a 10x10 grid using nested loops
# Or you can use a single loop and calculate the row and column

# In the loop, calculate or increment the number

# Use % determing the display, using fizzbuzz rules

# If you are displaying a number, calculate the sum of the digits and determine the color

# Call Text(app, text='...', grid=[col, row], color=...) to display something. 

# app.display()


from guizero import App, Text

# Create the app with a grid layout
app = App("Numbers Grid", layout="grid")

# Generate the 10x10 grid using nested loops
number = 1
for row in range(10):  # Rows 0 to 9
    for col in range(10):  # Columns 0 to 9
        if number % 15 == 0:
            # Divisible by 15
            display_text = '🐍'
            color = "black"  # Default color for icons
        elif number % 5 == 0:
            # Divisible by 5
            display_text = '🦡'
            color = "black"
        elif number % 3 == 0:
            # Divisible by 3
            display_text = '🍄'
            color = "black"
        else:
            # Not divisible by 3 or 5
            display_text = str(number)
            # Calculate the sum of digits to determine color
            digit_sum = sum(int(digit) for digit in str(number))
            if digit_sum % 2 == 0:
                color = "blue"
            else:
                color = "red"

        # Add the text to the app grid
        Text(app, text=display_text, grid=[col, row], color=color)

        # Increment the number
        number += 1

app.display()