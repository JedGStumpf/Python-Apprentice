"""
Infuriating Calculator

Let's write a calculator that's really hard to use

Ask the user for three things: 

1. A number
2. A second number
3. A math operation (add, subtract, multiply, divide)
4. Use if-elif-else statements to provide the desired math operation on the numbers and display the result.

If the user enters an unknown operation, display an error message. ( use messagebox.showerror() 

For the number, you can ask for a float or an integer with 
simpledialog.askfloat() or simpledialog.askinteger(), and for the math 
operation you can ask for a string with simpledialog.askstring().

"""

# Import the required modules

# Create a window object

# Hide the window, hint: use the withdraw method

# Ask the user for the first number 
first_num = int(input("First Number, Enter Your First Number"))

# Ask the user for the second number
second_num = int(input("Second Number, Enter Your Second Number"))

# Ask the user for the math operation
operation = input("Math Operation, Enter the math operation (add, subtract, multiply, divide)")

# Use if-elif-else statements to provide the desired math operation on the numbers and display the result.
if operation == "add":
    print(first_num + second_num)
elif operation == "subtract":
    print(first_num - second_num)
elif operation == "multiply":   
    print(first_num * second_num)
elif operation == "divide":
    print(first_num / second_num)
else:
    # Display an error message
    print("Unknown operation. Please enter add, subtract, multiply, or divide.")
# If the user enters an unknown operation, display an error message. ( use messagebox.showerror()

# Keep the window open
