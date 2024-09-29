"""
Write a Python program that asks the user for two numbers.
The program should display the sum of the two numbers.

In this program we will just give you the comments for
what you need to do. Look at the comments and the
code snippets in the previous lessons to figure out
how to complete the program.


"""

# Import the required modules
from tkinter import messagebox, simpledialog, Tk # import required modules

window = Tk()     # Create a window object
window.withdraw() # Hide the window
# Create a window object

# Hide the window, hint: use the withdraw method

# Ask the user for the first number   
first_num = simpledialog.askinteger("First Number", "Enter Your First Number")
second_num = simpledialog.askinteger("First Number", "Enter Your Second Number")

# Ask the user for the second number1


# Display the sum of the two numbers 
messagebox.showinfo("Answer", str(first_num+second_num))
# Keep the window open

