def print_board(board):
    print("  0 1 2")
    for i in range(3):
        print(i, board[str(0) + str(i)], board[str(1) + str(i)], board[str(2) + str(i)])


def make_move(player_token):
    valid = False
    while not valid:
        player_answer = input("Куда поставить " + player_token + "?: ")
        if player_answer not in board.keys():
            print("Недопустимый ход. Придерживайтесь диапазона 00-22.")
            continue

        if board[player_answer] in "X0":
            print("Эта клетка уже занята.")
            continue

        board[player_answer] = player_token
        valid = True


def check_win(board):
    win_coord = (("00", "01", "02"), ("10", "11", "12"), ("20", "21", "22"),
                 ("00", "10", "20"), ("01", "11", "21"), ("02", "12", "22"),
                 ("00", "11", "22"), ("02", "11", "20"))
    for each in win_coord:
        if board[each[0]] in "X0" and board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False


def main(board):
    counter = 0
    win = False
    while not win:
        print_board(board)
        if counter % 2 == 0:
            make_move("X")
        else:
            make_move("0")
        counter += 1
        if counter > 4:
            check_win_result = check_win(board)
            if check_win_result:
                print(check_win_result, "победил.")
                print_board(board)
                win = True
                break
            if counter == 9:
                print("Ничья.")
                print_board(board)
                break
    print("Игра окончена.")


board = {"00": "-", "10": "-", "20": "-", "01": "-", "11": "-", "21": "-", "02": "-", "12": "-", "22": "-"}
main(board)