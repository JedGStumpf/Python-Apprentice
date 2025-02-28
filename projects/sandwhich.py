"""
Fun project for St. James to dial in order of operations, loops, lists, etc.
"""

making_sandwhich = True
operation = []
ingredients = []

while making_sandwhich:
    instruct = input("Tell me what to do, press enter to pass, or type EXIT to finish:  ")
    if instruct.lower().startswith("e"):
        making_sandwhich = False
    else:

        if instruct != "":
            operation.append(instruct)
        else:
            operation.append(" ")

        food_item = input("What do you want to add to the sandwhich, or press enter to pass:  ")
        if food_item == "":
            ingredients.append(" ")
        else:
            ingredients.append(food_item)


finished = []
for i in range(len(operation)):
    finished.append(operation[i])
    finished.append(ingredients[i])


print("\n"*5)
print(f'These are my instructions:  {finished}')
print("Here were my step by step instructions:")

for i, x in enumerate(finished):
    if x != " ":
        print(i, x)

print("Enjoy the Sandwhich")
print("\n"*5)





