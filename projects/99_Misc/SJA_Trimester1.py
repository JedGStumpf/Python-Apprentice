"""
On your own follow the below instructions to show your 
code knowlege at the end of Trimester 1
"""

# 1.  Create 3 variables, 1 each of String, Int, and Boolean
my_str = "string"
num = 10
sigma = False
# 2.  Write a for loop that prints the numbers 1-100 except 
#           numbers that are divisable by 7
for x in range(1,101):
    if x % 7 == 0:
        print("")
    else:
        print(x)


# 3.  Write a for loop that prints every other letter 
#           of the string you created in the 1st task
count = 1
for x in my_str:
    if count % 2 == 0:
        print(my_str[count])
    count +=1



# 4.a  Create a function that takes in 2 arguments, both integers, 
#           and returns the sum of those 2 arguments

def add_nums(num1, num2):
    return num1 + num2


# 4.b. Call the function from task 4.a
add_nums(10, 10)


# EXTRA CREDIT !!!
# EC_1.a  Create a function that takes in a string as an argument   
#          and returns a list containing each letter of the string

def create_list(string):
    return list(string)


# EC_1.b. Call the function from task EC_1.a
create_list("Jed")

# EC_2.a. Create a function that takes a list of letters as an argument
#         and returns a string with all the letters in the list capitalized

# EC_2.b. Call the function from task EC_2.a


