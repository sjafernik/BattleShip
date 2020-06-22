def init_board():
    # inicjuje pustą planszę

    board_ship = {'A1': '0', 'A2': '0', 'A3': '0', 'A4': '0', 'A5': '0',
                  'B1': '0', 'B2': '0', 'B3': '0', 'B4': '0', 'B5': '0',
                  'C1': '0', 'C2': '0', 'C3': '0', 'C4': '0', 'C5': '0',
                  'D1': '0', 'D2': '0', 'D3': '0', 'D4': '0', 'D5': '0',
                  'E1': '0', 'E2': '0', 'E3': '0', 'E4': '0', 'E5': '0', }

    return board_ship


def display_board(board):
    # pokazuje zmiany na planszy

    pass


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
