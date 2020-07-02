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
        print(f"\nplease choose letter from {row_list[0]}-{row_list[-1]}")
        row = input(f"Enter your row coordinates {row_list[0]}-{row_list[-1]}: ").capitalize()

    row = row_list.index(row)  # make from letter an index of row

    # try catch ValueError if player enter something different than letter
    while True:
        try:
            col = int(input(f"\nEnter your col coordinates {begin}-{end - 1}: "))  # ask for a col from board
            break
        except ValueError:
            print(f"\nplease choose number between {begin} and {end - 1}")  # error when input is 22aaa

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

    ship_list = []  # list for possible ship cells
    board_with_ships = board
    direction = 0

    coordinate = player_input()
    row = coordinate[0]  # A-E
    col = coordinate[1]  # 1-5

    # player choose direction of his ship
    ship_placement = input("Do you want to place your ship horizontal right or vertical down? ").lower()

    while ship_placement != "horizontal" and ship_placement != "vertical":
        print("Please insert \"horizontal\" or \"vertical\"")
        ship_placement = input("Do you want to place your ship horizontal right or vertical down? ").lower()

    if ship_placement == "horizontal":
        direction = col
    elif ship_placement == "vertical":
        direction = row

    # check if ship is not longer than board
    while direction + ship > len(board_with_ships):
        print("Part of your ship is outside of board! Choose another place. ")
        place_your_one_ship(board, ship)

    # init temporary board to not increase our origin board in move_is_possible()
    temp_board = copy.deepcopy(board_with_ships)

    if ship_placement == "vertical":
        if move_is_possible(temp_board, row, col, ship, ship_placement):  # check neighbour cells
            for i in range(ship):
                ship_list.append(board_with_ships[row + i][col])  # adding possible ship cells to list

            if 'X' in ship_list:  # check possible cells
                print("choose another position")
                place_your_one_ship(board, ship)  # return to the begin of function

            else:
                for i in range(ship):
                    board_with_ships[row + i][col] = 'X'  # mark ship cells

        else:
            print("choose another position")
            place_your_one_ship(board, ship)  # if move_is_possible() is False return to the begin of function

    # the same as vertical above
    elif ship_placement == "horizontal":
        if move_is_possible(temp_board, row, col, ship, ship_placement):
            for i in range(ship):
                ship_list.append(board_with_ships[row][col + i])

            if 'X' in ship_list:
                print("choose another position")
                place_your_one_ship(board, ship)

            else:
                for i in range(ship):
                    board_with_ships[row][col + i] = 'X'

        else:
            print("choose another position")
            place_your_one_ship(board, ship)

    display_board(board_with_ships)

    return board_with_ships


def yours_ship():
    # function return board with all ships

    your_board_with_ships = init_board()
    display_board(your_board_with_ships)

    # ask where to place one 3-deck ship
    print("\nplace your's 3-deck ship")
    ship = 3
    your_board_with_ships = place_your_one_ship(your_board_with_ships, ship)

    # ask where to place two 2-deck ships
    print("\nplace your's two 2-deck ship")
    for i in range(0, 2):
        ship = 2
        your_board_with_ships = place_your_one_ship(your_board_with_ships, ship)

    # ask where to place three 1-deck ships
    print("\nplace three of your's one deck ship")
    for i in range(0, 3):
        ship = 1
        your_board_with_ships = place_your_one_ship(your_board_with_ships, ship)

    return your_board_with_ships


def mark_shoot_place(my_shoot_board, enemy_board):
    missed_shot = 'M'
    hit_ship = 'H'
    sunk_ship = 'S'
    coordinates = player_input()

    # enemy_board = enemy_board
    # my_shoot_board = my_shoot_board

    if my_shoot_board[coordinates[0]][coordinates[1]] != '0' and my_shoot_board[coordinates[0]][coordinates[1]] != 'X':
        print("You have already shot this spot.")

    else:
        for i in range(0, len(enemy_board)):
            enemy_board[i].insert(0, "0")
            enemy_board[i].append("0")

        enemy_board.insert(0, ["0", "0", "0", "0", "0", "0", "0"])
        enemy_board.append(["0", "0", "0", "0", "0", "0", "0"])

        neib_cells = [[enemy_board[coordinates[0] + 2][coordinates[1] + 1]],
                      [enemy_board[coordinates[0]][coordinates[1] + 1]],
                      [enemy_board[coordinates[0] + 1][coordinates[1] + 2]],
                      [enemy_board[coordinates[0] + 1][coordinates[1]]]]

        if enemy_board[coordinates[0] + 1][coordinates[1] + 1] == 'X':
            if ['X'] in neib_cells:
                my_shoot_board[coordinates[0]][coordinates[1]] = hit_ship
            else:
                my_shoot_board[coordinates[0]][coordinates[1]] = sunk_ship

        elif enemy_board[coordinates[0] + 1][coordinates[1] + 1] == '0':
            my_shoot_board[coordinates[0]][coordinates[1]] = missed_shot


#     # 0 indicates an undiscovered tile
#     # M indicates a missed shot
#     # H indicates a hit ship part
#     # S indicates a sunk ship part


def winner_check():
    # sprawdza czy na którejś z tablic nie ma X
    # jeśli nie ma to drugi gracz wygrał

    pass


def game():
    pass


def main():
    print("Welcome to Battle ship game!")

    player_one = input("What is first player name? ")
    player_two = input("What is second player name? ")

    print(f"{player_one} please set your ships on board\n")
    player_one_ship_board = yours_ship()

    print(f"{player_two} please set your ships on board\n")
    player_two_ship_board = yours_ship()





main()



# player2_ship_board = [["0", "X", "0", "0", "X"],
#                       ["X", "0", "0", "0", "0"],
#                       ["X", "0", "0", "0", "0"],
#                       ["X", "0", "0", "0", "0"],
#                       ["0", "X", "0", "0", "0"]]
