import copy


def init_board():
    # initialized empty game board
    board_ship = [["0", "0", "0", "0", "0"],
                  ["0", "0", "0", "0", "0"],
                  ["0", "0", "0", "0", "0"],
                  ["0", "0", "0", "0", "0"],
                  ["0", "0", "0", "0", "0"]]

    return board_ship


def display_board(board):
    # display board from parameter

    # printing set of numbers on the top of board
    for i in range(0, len(board)):
        print(f"   {i + 1}", end="")

    print()

    # printing board index by index split by " | "
    for i in range(0, len(board)):
        temp_list = " | ".join(board[i])
        print(f" {chr(65 + i)} {temp_list} ")

        # print lines for separating rows
        if i < len(board) - 1:
            marks = "---+" * (len(board) - 1)
            print(f"  {marks}---")


def player_input():
    # def for coordinate input with a board
    row_list = ['A', 'B', 'C', 'D', 'E']  # list of board rows for input
    begin = 1  # the first column of the board
    end = 6  # the last column of the board
    col = None

    row = input(
        f"\nEnter your row coordinates {row_list[0]}-{row_list[-1]}: ").capitalize()  # ask for a row from A to E

    while row not in row_list:  # check if input is in board
        print(f"\nPlease choose letter from {row_list[0]}-{row_list[-1]}")
        row = input(f"Enter your row coordinates {row_list[0]}-{row_list[-1]}: ").capitalize()

    row = row_list.index(row)  # make from letter an index of row

    # try catch ValueError if player enter something different than letter
    while True:
        try:
            col = int(input(f"\nEnter your col coordinates {begin}-{end - 1}: "))  # ask for a col from board
            break
        except ValueError:
            print(f"\nPlease choose number between {begin} and {end - 1}")  # error when input is 22aaa

    while col not in range(begin, end):  # check if input is in board
        col = int(input(f"\nEnter your col coordinates {begin}-{end - 1}: "))

    col = col - 1  # -1 for make from input an index

    coordinate = [row, col]

    return coordinate


def move_is_possible(board, row, col, ship, ship_placement):
    # return True or False if move is possible

    possible_move = ""
    origin_board = board
    board_ship = copy.deepcopy(origin_board)

    # increase board to catch IndexOutOfRange error
    board_ship.insert(0, ["0", "0", "0", "0", "0", "0", "0"])
    board_ship.append(["0", "0", "0", "0", "0", "0", "0"])

    # adding 0 in begin and end nested list to increase them
    for i in range(0, len(board_ship)):
        board_ship[i].insert(0, "0")
        board_ship[i].append("0")

    # check if there are any X in neighbour cells in vertical or horizontal position
    if ship_placement == "vertical":
        for i in range(ship):
            possible_move = ((board_ship[row + i + 1][col + 2] == "0")
                             and (board_ship[row + i + 1][col] == "0")
                             and (board_ship[row + i][col + 1] == "0")
                             and (board_ship[row + i + 2][col + 1] == "0"))

            if not possible_move:
                return False

    elif ship_placement == "horizontal":
        for i in range(ship):
            possible_move = ((board_ship[row + 1][col + i + 2] == "0")
                             and (board_ship[row + 1][col + i] == "0")
                             and (board_ship[row][col + i + 1] == "0")
                             and (board_ship[row + 2][col + i + 1] == "0"))

            if not possible_move:
                return False

    return possible_move


def place_your_one_ship(board, ship):
    # ask player for a coordinates and direction and if its possible set one ship on board
    flag = True  # making loop to catch error input
    length_flag = True  # making loop to catch IndexOutOfRange
    ship_list = []  # list for possible ship cells
    board_with_ships = board
    direction = 0

    while flag:
        while length_flag:
            coordinate = player_input()
            row = coordinate[0]  # A-E
            col = coordinate[1]  # 1-5

            # player choose direction of his ship 
            if ship == 1:
                ship_placement = "horizontal"
            else:
                ship_placement = input("\nDo you want to place your ship horizontal right or vertical down? ").lower()

            if ship_placement != "horizontal" and ship_placement != "vertical":
                print("Please insert \"horizontal\" or \"vertical\"")
                ship_placement = input("\nDo you want to place your ship horizontal right or vertical down? ").lower()

            if ship_placement == "horizontal":
                direction = col
            elif ship_placement == "vertical":
                direction = row

            # check if ship is not longer than board
            if direction + ship > len(board_with_ships):
                print("\nPart of your ship is outside of board! Choose another place.")

            else:
                length_flag = False

        # init temporary board to not increase our origin board in move_is_possible()
        temp_board = copy.deepcopy(board_with_ships)

        if ship_placement == "vertical":
            if move_is_possible(temp_board, row, col, ship, ship_placement):  # check neighbour cells
                for i in range(ship):
                    ship_list.append(board_with_ships[row + i][col])  # adding possible ship cells to list

                if 'X' in ship_list:  # check possible cells
                    print("\nChoose another position\n")
                    flag = True
                    length_flag = True

                else:
                    for i in range(ship):
                        board_with_ships[row + i][col] = 'X'  # mark ship cells
                        flag = False
            else:
                print("\nChoose another position\n")
                length_flag = True

        # the same as vertical above
        elif ship_placement == "horizontal":
            if move_is_possible(temp_board, row, col, ship, ship_placement):
                for i in range(ship):
                    ship_list.append(board_with_ships[row][col + i])

                if 'X' in ship_list:
                    print("\nChoose another position\n")
                    length_flag = True

                else:
                    for i in range(ship):
                        board_with_ships[row][col + i] = 'X'
                        flag = False

            else:
                print("\nChoose another position\n")
                length_flag = True

    display_board(board_with_ships)

    return board_with_ships


def yours_ship():
    # function return board with all ships
    list_of_ships = [3, 2, 2, 1, 1, 1]  # list of all ships
    your_board_with_ships = init_board()
    display_board(your_board_with_ships)

    for i in list_of_ships:  # loop for place all ships
        print(f"\nPlace your's {i}-deck ship")
        ship = i
        your_board_with_ships = place_your_one_ship(your_board_with_ships, ship)

    return your_board_with_ships


def mark_shoot_place(my_shoot_board, enemy_board):
    missed_shot = 'M'
    hit_ship = 'H'
    sunk_ship = 'S'
    coordinates = player_input()

    # enemy_board = enemy_board
    # my_shoot_board = my_shoot_board

    enemy_board_with_ships = copy.deepcopy(enemy_board)

    if my_shoot_board[coordinates[0]][coordinates[1]] != '0' and my_shoot_board[coordinates[0]][coordinates[1]] != 'X':
        print("You have already shot this spot.")

    else:
        for i in range(0, len(enemy_board_with_ships)):
            enemy_board_with_ships[i].insert(0, "0")
            enemy_board_with_ships[i].append("0")

        enemy_board_with_ships.insert(0, ["0", "0", "0", "0", "0", "0", "0"])
        enemy_board_with_ships.append(["0", "0", "0", "0", "0", "0", "0"])

        neib_cells = [[enemy_board_with_ships[coordinates[0] + 2][coordinates[1] + 1]],
                      [enemy_board_with_ships[coordinates[0]][coordinates[1] + 1]],
                      [enemy_board_with_ships[coordinates[0] + 1][coordinates[1] + 2]],
                      [enemy_board_with_ships[coordinates[0] + 1][coordinates[1]]]]

        if enemy_board_with_ships[coordinates[0] + 1][coordinates[1] + 1] == 'X':
            if ['X'] in neib_cells:
                my_shoot_board[coordinates[0]][coordinates[1]] = hit_ship
                enemy_board[coordinates[0]][coordinates[1]] = hit_ship
            else:
                my_shoot_board[coordinates[0]][coordinates[1]] = sunk_ship
                enemy_board[coordinates[0]][coordinates[1]] = sunk_ship

        elif enemy_board_with_ships[coordinates[0] + 1][coordinates[1] + 1] == '0':
            my_shoot_board[coordinates[0]][coordinates[1]] = missed_shot
            enemy_board[coordinates[0]][coordinates[1]] = missed_shot

    display_board(my_shoot_board)


def winner_check(board, player):
    check_board = board
    ship = "X"

    is_winner = any(ship in sublist for sublist in check_board)

    if not is_winner:
        print(f"{player} IS WINNER!")

    return is_winner


def game():
    player_one = input("What is the first player name? ")
    player_two = input("What is the second player name? ")

    print(f"\n {player_one} please set your ships on the board.\n")
    player_one_ship_board = yours_ship()

    print(f"\n {player_two} please set your ships on the board.\n")
    player_two_ship_board = yours_ship()

    player_one_shoot_board = init_board()
    player_two_shoot_board = init_board()

    winner = False

    while not winner:
        mark_shoot_place(player_one_shoot_board, player_two_ship_board)
        winner = winner_check(player_two_ship_board, player_one)

        mark_shoot_place(player_two_shoot_board, player_one_ship_board)
        winner = winner_check(player_one_ship_board, player_two)


def main():
    print("Welcome to Battle ship game!")

    game()


# TESTING TESTING TESTING TESTING TESTING TESTING TESTING TESTING

# player_one = input("What is the first player name? ")
# player_two = input("What is the second player name? ")
#
# player_one_ship_board = [["0", "X", "0", "0", "X"],
#                          ["X", "0", "0", "0", "0"],
#                          ["X", "0", "0", "0", "0"],
#                          ["X", "0", "0", "0", "0"],
#                          ["0", "X", "0", "0", "0"]]
#
# player_two_ship_board = [["0", "X", "0", "0", "X"],
#                          ["X", "0", "0", "0", "0"],
#                          ["X", "0", "0", "0", "0"],
#                          ["X", "0", "0", "0", "0"],
#                          ["0", "X", "0", "0", "0"]]
#
# player_one_shoot_board = init_board()
# player_two_shoot_board = init_board()
#
# winner = True
#
# while winner:
#     mark_shoot_place(player_one_shoot_board, player_two_ship_board)
#     winner = winner_check(player_two_ship_board, player_one)
#
#     mark_shoot_place(player_two_shoot_board, player_one_ship_board)
#     winner = winner_check(player_one_ship_board, player_two)
