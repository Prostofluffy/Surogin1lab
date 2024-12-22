def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")


def check_winner(board):
    winning_positions = [

        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],

        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],

        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    ]

    for positions in winning_positions:
        line = [board[x][y] for x, y in positions]
        if line == ["X", "X", "X"]:
            return "X"
        if line == ["O", "O", "O"]:
            return "O"

    for row in board:
        if " " in row:
            return None

    return "Draw"


def is_valid_move(board, x, y):
    return 0 <= x <= 2 and 0 <= y <= 2 and board[x][y] == " "


def get_player_input(player, board):
    while True:
        try:
            move = input(f"Ходит {player} (введите строку и столбец через пробел): ")
            x, y = map(int, move.split())
            if is_valid_move(board, x, y):
                return x, y
            else:
                print("Некорректный ход! Ячейка занята или координаты некорректны.")
        except (ValueError, IndexError):
            print("Ошибка ввода.Вводите два числа от 0 до 2 через пробел.")


def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Добро пожаловать в игру Крестики-Нолики!")
    print("Игровое поле 3x3, строки и столбцы нумеруются от 0 до 2.\n")
    print_board(board)

    while True:
        x, y = get_player_input(current_player, board)
        board[x][y] = current_player

        print_board(board)

        result = check_winner(board)
        if result:
            if result == "Draw":
                print("Игра окончена! Ничья!")
            else:
                print(f"Поздравляем! {result} победил!")
            break

        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    tic_tac_toe()
