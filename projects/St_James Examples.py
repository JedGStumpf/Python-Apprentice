#Code a for loop that creates a 2d array 3x3 with numeric values

board = [[None, None, None],
         [3, 4, 5],
         [6, 7, 8]]

for row in board:
    print(row)
# print(board[0])

# print(board[0][2])
# print(board[2][2])

# print(board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][1] is not None)


def none_function():
    x = 0
    print(x)
    # return x

print(none_function())


def say_my_name(name):
    print(f"Hello {name}")

# say_my_name("St. James")

def print_my_list(my_list):

    print(my_list)

# print("Columns below")
# for column in board:
#     print_my_list(column)
        
# print(board[1][2])


row = None

# if row:
#     print("True")
# else:
#     print("False")





my_dictionary = {}


my_dictionary["name"] = "St. James"
my_dictionary["age"] = 25


# print(my_dictionary)

del my_dictionary["age"]
# print(my_dictionary)


db = {}


def add_to_db(db, key, value):
    db[key] = value


# print(db)

add_to_db(db, "name", "St. James")
add_to_db(db, "age", "25")

# print(db)

# del db["name"]
# print(db)




def is_funny(definition):
    for key, value in db.items():
        # print(f"Key: {key}, Value: {value}")
        if value in definition:
            # return True
            print(f"{value} is funny")

        else:
            print("Not funny")
    
# is_funny("St. James")
# is_funny("this is wrong")


# 5/9/2025


rooms = (1, 2, 3, 4, 5)

checked_in_rooms = {1:"Pelayo"}

# for room in rooms:
#     if room in checked_in_rooms.keys():
#         print(f"Room {room} is checked in")
#     else:
#         print(f"Room {room} is available")


name = "St. James"
age = 25
# print(f"{name} {age} ")
# print(name + " " + str(age))


# 5/23/2025



from string import ascii_lowercase as lettters

alphabet = [letter for letter in lettters]
# print(alphabet)


rooms = [1, 2, 3, 4, 5]

# cust_choice = int(input("Enter room number: "))

# name = input("Enter your name: ")

# occupied = {}

# if cust_choice in rooms:
#     checked_room = rooms.pop(rooms.index(cust_choice))
#     occupied[checked_room] = name
# else:
#     print("Room not available")

# print(occupied)

# print(rooms)
