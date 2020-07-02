import copy


def init_board():
    # initialized empty game board

    # dictionary version
    # board_ship = {'A1': '0', 'A2': '0', 'A3': '0', 'A4': '0', 'A5': '0',
    #               'B1': '0', 'B2': '0', 'B3': '0', 'B4': '0', 'B5': '0',
    #               'C1': '0', 'C2': '0', 'C3': '0', 'C4': '0', 'C5': '0',
    #               'D1': '0', 'D2': '0', 'D3': '0', 'D4': '0', 'D5': '0',
    #               'E1': '0', 'E2': '0', 'E3': '0', 'E4': '0', 'E5': '0', }

    # list version
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

    row = input(
        f"\nEnter your row coordinates {row_list[0]}-{row_list[-1]}: ").capitalize()  # ask for a row from A to E

    while row not in row_list:  # check if input is in board
        row = input(f"\nEnter your row coordinates {row_list[0]}-{row_list[-1]}: ").capitalize()

    row = row_list.index(row)  # make from letter an index of row

    col = int(input(f"Enter your col coordinates {begin}-{end - 1}: "))  # ask for a col from board

    while col not in range(begin, end):  # check if input is in board
        col = int(input(f"Enter your col coordinates {begin}-{end - 1}: "))

    col = col - 1  # -1 for make from input an index

    coordinate = [row, col]

    return coordinate


def move_is_possible(board):
    # check if field is free

    coordinates = player_input()
    row = coordinates[0]
    col = coordinates[1]

    origin_board = board
    board_ship = copy.deepcopy(origin_board)

    for i in range(0, len(board_ship)):
        board_ship[i].insert(0, "0")
        board_ship[i].append("0")

    board_ship.insert(0, ["0", "0", "0", "0", "0", "0", "0"])
    board_ship.append(["0", "0", "0", "0", "0", "0", "0"])

    if board_ship[row + 1][col + 1] != "0":
        print("This place is already taken!")
        return

    possible_move = ((board_ship[row + 1][col + 2] == "0")
                     and (board_ship[row + 1][col] == "0")
                     and (board_ship[row][col + 1] == "0")
                     and (board_ship[row + 2][col + 1] == "0"))

    return possible_move


def place_your_one_ship(board, ship):
    def place_your_one_ship(board, ship):
    # ask player if he want:
    # horizontal_right
    # vertical_down
    # ship placement
    ship_list=[]
    board_with_ships = board
    direction = 0

    coordinate = player_input()
    row = coordinate[0]
    col = coordinate[1]

    ship_placement = input("Do you want to place your ship horizontal right or vertical down? ").lower()

    while ship_placement != "horizontal" and ship_placement != "vertical":
        print("please insert \"horizontal\" or \"vertical\"")
        ship_placement = input("Do you want to place your ship horizontal right or vertical down? ").lower()

    if ship_placement == "horizontal":
        direction = col
    elif ship_placement == "vertical":
        direction = row

    while direction + ship > len(board_with_ships):
        place_your_one_ship(board, ship)

    temp_board = copy.deepcopy(board_with_ships)
    
    # sprawdzić czy są X po bokach(move_is_possible() ?)
    # sprawdzić czy są X w miejscach gdzie będziemy wstawiać
    if ship_placement == "vertical":
            if move_is_possible(temp_board, direction, row, col, ship) == True: #    TO JEST źLE
                for i in range (ship):
                    ship_list.append(board_with_ships[row + i][col])
                if 'X' in ship_list:
                    print("choose another position_3")
                    place_your_one_ship(board, ship)

                else:
                    for i in range (ship):
                        board_with_ships[row + i][col] = 'X'
                        display_board(board_with_ships)
                        
            else:
                print("choose another position_4")
                place_your_one_ship(board, ship)

    elif ship_placement == "horizontal":
            if move_is_possible(temp_board, direction, row, col, ship) == True: #    TO JEST źLE
                for i in range (ship):
                    ship_list.append(board_with_ships[row][col+i])
                if 'X' in ship_list:
                    print("choose another position_2")
                    place_your_one_ship(board, ship)

                else:
                    for i in range (ship):
                        board_with_ships[row][col+i] = 'X'
                        display_board(board_with_ships)
            else:
                print("choose another position_5")
                place_your_one_ship(board, ship)

    return board_with_ships


def yours_ship():
    display_board(init_board())

    print("\nplace your's 3-deck ship")
    ship = 3
    your_board = place_your_one_ship(init_board(), ship)
    display_board(your_board)

    print("\nplace your's two 2-deck ship")
    for i in range(0, 2):
        ship = 2
        your_board = place_your_one_ship(your_board, ship)
        display_board(your_board)

    print("\nplace three of your's one deck ship")
    for i in range(0, 3):
        ship = 1
        your_board = place_your_one_ship(your_board, ship)
        display_board(your_board)

    return your_board


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


def end_game():
    # wypisuje zwycięzcę i kończy grę
    # wychodzi z pętli

    pass


def game():
    pass


# print(move_is_possible(board_with_ships))

player2_ship_board = [["0", "X", "0", "0", "X"],
                      ["X", "0", "0", "0", "0"],
                      ["X", "0", "0", "0", "0"],
                      ["X", "0", "0", "0", "0"],
                      ["0", "X", "0", "0", "0"]]
#
# for i in range(0, 4):
#     player1_shoot_board = init_board()
#
#     mark_shoot_place(player1_shoot_board, player2_ship_board)
#
#     display_board(player1_shoot_board)
#
#

display_board(player2_ship_board)
print(move_is_possible(player2_ship_board))
display_board(player2_ship_board)
