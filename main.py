# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

symbols = {"user1": "X", "user2": "O"}
def ask_user1(board):
    # user 1 uses X
    print("User 1 : X")
    row = int(input("Enter Row value\n"))
    col = int(input("Enter Column Value\n"))
    if board[row][col] == "E":
        board[row][col] = "X"
        return True
    else:
        return False


def ask_user2(board):
    # user 2 uses O
    print("User 2 : O")
    row = int(input("Enter Row value\n"))
    col = int(input("Enter Column Value\n"))
    if board[row][col] == "E":
        board[row][col] = "O"
        return True
    else:
        return False

def print_board(board):
    for row in board:
        print(row[0], row[1], row[2])


def switch_user(current):
    if current == "user1":
        return "user2"
    else:
        return "user1"


def check_win(board, current_user):
    symbol = symbols.get(current_user)

    # check row
    for row in board:
        win = True
        for r in row:
            if r != symbol:
                win = False
        if win:
            return True

    # check col
    for index in range(3):
        win = True
        for j in range(3):
            if board[j][index] != symbol:
                win = False
        if win:
            return True

    # check diagonal
    if (board[0][0] == symbol) and (board[1][1] == symbol) and (board[2][2] == symbol):
        return True

    if (board[0][2] == symbol) and (board[1][1] == symbol) and (board[2][0] == symbol):
        return True

    return False


def tictactoe():
    print("User 1 uses X")
    print("User 2 uses O")

    print("E represents empty location")
    board = [["E", "E", "E"], ["E", "E", "E"], ["E", "E", "E"]]
    print(f"current board is:")

    win = False
    curr_user = "user1"
    while win is False:
        print_board(board)
        if curr_user == "user1":
            ret = ask_user1(board)
        else:
            ret = ask_user2(board)

        if check_win(board, curr_user):
            win = True
            break
        if ret:
            curr_user = switch_user(curr_user)

    if win:
        print(f"Congratulations, {curr_user} won!")
        print(board)
    else:
        print("Its a tie")
    return


if __name__ == '__main__':
    tictactoe()

