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

    board_ship = board

    for i in range(0, len(board_ship)):
        board_ship[i].insert(0, "0")
        board_ship[i].append("0")

    board_ship.insert(0, ["0", "0", "0", "0", "0", "0", "0"])
    board_ship.append(["0", "0", "0", "0", "0", "0", "0"])

    if board_ship[row][col] != "0":
        print("This place is already taken!")
        return

    possible_move = ((board_ship[row + 1][col + 2] == "0")
                    and (board_ship[row + 1][col] == "0")
                    and (board_ship[row][col + 1] == "0")
                    and (board_ship[row + 2][col + 1] == "0"))

    return possible_move


def place_your_one_ship(board, ship):
    # zaznacza ustawienie statków z wykorzystaniem is_possible_to_mark()
    # musi zapisać współrzędne położenia statku w liście
    # parametr ship będzie przyjmował długość statku

    # trzeba dopisać warunki żeby stawiał w linin iksy
    while ship != 0:
        coordinate = player_input()
        row = coordinate[0]
        col = coordinate[1]

        temp_board = board

        if temp_board[row][col] == '0':
            temp_board[row][col] = 'X'

        ship -= 1

    return temp_board


def yours_ship():
    print("place your long ship")
    ship = 3
    your_board = place_your_one_ship(init_board(), ship)
    display_board(your_board)

    ship = 2
    your_board = place_your_one_ship(your_board, ship)
    display_board(your_board)

    ship = 1
    your_board = place_your_one_ship(your_board, ship)
    display_board(your_board)


def shoot():
    # SZCZELANIE
    pass


def mark_shoot_place(coordinates):
    missed_shot = 'M'
    hit_ship = 'H'
    sunk_ship = 'S'
    neib_cells = []
    list_end = len(board_with_ships) - 1

    if coordinates[0] == 0:
        down_one = [board_with_ships[coordinates[0] + 1][coordinates[1]]]
        neib_cells.append(down_one)

    elif coordinates[0] == 4:
        up_one = [board_with_ships[coordinates[0] - 1][coordinates[1]]]
        neib_cells.append(up_one)

    else:
        down_one = [board_with_ships[coordinates[0] + 1][coordinates[1]]]
        neib_cells.append(down_one)
        up_one = [board_with_ships[coordinates[0] - 1][coordinates[1]]]
        neib_cells.append(up_one)

    if coordinates[1] == 0:
        right_one = [board_with_ships[coordinates[0]][coordinates[1] + 1]]
        neib_cells.append(right_one)

    elif coordinates[1] == 4:
        left_one = [board_with_ships[coordinates[0]][coordinates[1] - 1]]
        neib_cells.append(left_one)

    else:
        right_one = [board_with_ships[coordinates[0]][coordinates[1] + 1]]
        left_one = [board_with_ships[coordinates[0]][coordinates[1] - 1]]
        neib_cells.append(left_one)
        neib_cells.append(right_one)

    if board_with_ships[coordinates[0]][coordinates[1]] == 'X':
        if ['X'] in neib_cells:
            board_with_ships[coordinates[0]][coordinates[1]] = hit_ship
        else:
            board_with_ships[coordinates[0]][coordinates[1]] = sunk_ship


    elif board_with_ships[coordinates[0]][coordinates[1]] == '0':
        board_with_ships[coordinates[0]][coordinates[1]] = missed_shot


# def mark_shoot_place():
#     # 0 indicates an undiscovered tile
#     # M indicates a missed shot
#     # H indicates a hit ship part
#     # S indicates a sunk ship part
#
#     pass


def end_game():
    # wypisuje zwycięzcę i kończy grę
    # wychodzi z pętli

    pass


def game():
    pass


# # example of board with ships for tests
# board_with_ships = [["0", "X", "0", "0", "X"],
#                     ["X", "0", "0", "0", "0"],
#                     ["X", "0", "0", "0", "0"],
#                     ["X", "0", "0", "0", "0"],
#                     ["0", "X", "0", "0", "0"]]
#
# print(move_is_possible(board_with_ships))
