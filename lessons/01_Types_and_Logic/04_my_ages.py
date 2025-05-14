
"""
Am I Big Yet?

Ask the user's age then use an if-elif-else statement to 
tell the user what age groups the user is in. The groups are:

0-2: Baby
3-5: Toddler
6-12: Child
13-19: Teen
20-64: Adult
65+: Senior

Except, if the user is the same age as you, print "You are pretty awesome!"
"""

from tkinter import messagebox, simpledialog, Tk # import required modules

window = Tk()     # Create a window object
window.withdraw() # Hide the window

# Here is how you ask the user's age in integer format. 
# The first argument is the title of the window, the second is the message to the user.
# age = simpledialog.askinteger("Your Age", "How old are you?")  # ;

# You could also ask the user for a float with simpledialog.askfloat()
# ( but only do one of them, not both)
# age =  simpledialog.askfloat("Your Age", "How old are you?")  # ;
age = int(input("How old are you?"))  # ;  # This is a way to ask for an integer without using tkinter
# Here is how you show the user a message window
# The first parameter is the title of the window, 
# the second is the message to show the user.

message = ""
# messagebox.showinfo('What you are', "You are a baby.")

if age < 2:
    message = "You are a baby."
elif age < 5:
    message = "You are a toddler."
elif age < 13:
    message = "You are a child."
elif age < 20:
    message = "You are a teen."
elif age < 65:
    message = "You are an adult."
elif age >= 65:
    message = "You are a senior."
elif age == 12:
    message = "You are pretty awesome!"
else:
    message = "Um, I don't know what you are."


# messagebox.showinfo('What you are', message)
print(message)  # Print the message to the console
window.mainloop()  # Keeps the window open


# TODO: 
# Try to write your program so you only need to use one messagebox.showinfo() function.
