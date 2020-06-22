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
