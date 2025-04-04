#Code a for loop that creates a 2d array 3x3 with numeric values

board = [[0, 1, 2],
         [3, 4, 5],
         [6, 7, 8]]


# print(array[0][2])
print(board[2][2])


def say_my_name(name):
    print(f"Hello {name}")

say_my_name("St. James")

def print_my_list(my_list):
    print(my_list)

print("Columns below")
for column in board:
    print_my_list(column)
        
print(board[1][2])


