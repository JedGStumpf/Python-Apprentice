# January 24th Code Challenge

# Using a for loop, reverse this string:

# forward = "forward"
# rev = ""
# # Your output should be "drawrof"

# for letter in forward[::-1]:
#     #print(letter)
#     rev += letter
# print(rev)


# rev = rev[::-1]
# print(rev)

# rev = reversed()
# print(rev)

#Useful String Methods

testing = "This is a String to Test String Methods"

print(testing)
# We can print a blank line with a blank print() function call
print()

#Or we can add a newline character where we want a new line to be printed with \n
print(f"Change all letters to uppercase \n with .upper():  {testing.upper()}")

print(f"Change all\n letters to lowercase with .lower():  {testing.lower()} \n")

print(f"Change the format to print as a Title with .title() {testing.title()} \n")

print(f"We can find the length of a string with len():  {len(testing)} \n")

# len() also works on lots of other types such as lists:
mylist = [0, 1, 2, 3, 4, 5, 6]

print(f"len on a list:  {len(mylist)}")

print(f"Python will let you check the type of pretty much anything with type():  {type(testing)}")

print(f"We can see if a character is in a string with the in keyword: {"z" in testing}")

print(f"The in keyword is very useful, it works on many data structures here's lists: {6 in mylist}")

print(f"We can find the index of an item in strings and other data structures with .index(): {testing.index("")}")

if "z" in testing:
    print(testing.index("z"))
else:
    print("Not Found")

