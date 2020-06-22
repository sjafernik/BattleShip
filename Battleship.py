row_list = ['A', 'B', 'C', 'D', 'E'] #list of board rows for input
begin = 1 #the fisrt column of the board
end = 6  #the last column of the board

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

    for i in range(0, len(board)):
        print(f"   {i + 1}", end="")

    print()

    for i in range(0, len(board)):
        temp_list = " | ".join(board[i])
        print(f" {chr(65 + i)} {temp_list}")

        if i < len(board) - 1:
            marks = "---+" * (len(board) - 1)
            print(f"  {marks}---")


# tu tak na dziko wywołuje funkje żeby sprawdzić czy działa
display_board(init_board())

def player_input(): #def for coordinate input with a board

    row=input("\nEnter your row coordinates (A-E): ").capitalize() #ask for a row from A to E

    while row not in row_list: #check if input is in board
        row=input("\nEnter your row coordinates (A-E): ").capitalize()

    row = row_list.index(row) #make from letter an index of row

    col = int(input("Enter your col coordinates (1-5): ")) #ask for a col from board
    while col not in range(begin, end): #check if input is in board
        col = int(input("Enter your col coordinates (1-5): "))
    
    col = col-1 # -1 for make from input an index


def is_possible_to_mark(board):
    # na etapie ustawiania statków sprawdza czy statki się ze sobą nie stykają

    pass


def place_your_ship(ship):
    # zaznacza ustawienie statków z wykorzystaniem is_possible_to_mark()
    # musi zapisać współrzędne położenia statku w liście
    # parametr ship będzie przyjmował długość statku

    pass


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
