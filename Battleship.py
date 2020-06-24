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

    row = input(f"\nEnter your row coordinates {row_list[0]}-{row_list[-1]}: ").capitalize()  # ask for a row from A to E

    while row not in row_list:  # check if input is in board
        row = input(f"\nEnter your row coordinates {row_list[0]}-{row_list[-1]}: ").capitalize()

    row = row_list.index(row)  # make from letter an index of row

    col = int(input(f"Enter your col coordinates {begin}-{end-1}: "))  # ask for a col from board

    while col not in range(begin, end):  # check if input is in board
        col = int(input(f"Enter your col coordinates {begin}-{end-1}: "))

    col = col - 1  # -1 for make from input an index

    coordinate = [row, col]

    return coordinate


def is_possible_to_mark(board):
    # check if field is free
    pass


def place_your_ship(ship):
    def place_your_ship():
    # zaznacza ustawienie statków z wykorzystaniem is_possible_to_mark()
    # musi zapisać współrzędne położenia statku w liście
    # parametr ship będzie przyjmował długość statku
    begin = 1  # the first column of the board
    end = 6  # the last column of the board
    ship='X'
    board_ship_with_x = [["0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0"]]
    row_list = ['A', 'B', 'C', 'D', 'E']  # list of board rows for input
    row = input(f"\nEnter your row coordinates {row_list[0]}-{row_list[-1]}: ").capitalize()  # ask for a row from A to E
    while row in row_list:
        row = row_list.index(row)  # make from letter an index of row
        col = int(input(f"Enter your col coordinates {begin}-{end-1}: "))  # ask for a col from board
        while col in range(begin, end):  # check if input is in board
            col = col - 1
            coordinate=[row,col]
            if board_ship_with_x[coordinate[0]][coordinate[1]] == '0':
                board_ship_with_x[coordinate[0]][coordinate[1]] ==ship
                print(board_ship_with_x[coordinate[0]][coordinate[1]])
                print(board_ship_with_x)


def shoot():
    # SZCZELANIE
    pass


def mark_shoot_place():
    # 0 indicates an undiscovered tile
    # M indicates a missed shot
    # H indicates a hit ship part
    # S indicates a sunk ship part

    pass


def end_game():
    # wypisuje zwycięzcę i kończy grę
    # wychodzi z pętli

    pass


def game():
    pass


# example of board with ships for tests
board_with_ships = [["0", "X", "X", "0", "X"],
                    ["X", "0", "0", "0", "0"],
                    ["X", "0", "X", "X", "0"],
                    ["X", "0", "0", "0", "0"],
                    ["0", "X", "0", "X", "0"]]

coordinates = player_input()
print(coordinates)
