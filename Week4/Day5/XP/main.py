board = [' ' for x in range(9)]

def display_board():
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()

def player_input(player):
    print("Player {}'s turn. Which space do you want to place your mark? (1-9)".format(player))
    choice = int(input("Enter the number of the space: ").strip())
    if board[choice - 1] == ' ':
        board[choice - 1] = player
    else:
        print("That space is already taken. Try again.")
        player_input(player)

def check_win(player):
    if (
        (board[0] == player and board[1] == player and board[2] == player) or
        (board[3] == player and board[4] == player and board[5] == player) or
        (board[6] == player and board[7] == player and board[8] == player) or
        (board[0] == player and board[3] == player and board[6] == player) or
        (board[1] == player and board[4] == player and board[7] == player) or
        (board[2] == player and board[5] == player and board[8] == player) or
        (board[0] == player and board[4] == player and board[8] == player) or
        (board[2] == player and board[4] == player and board[6] == player)
    ):
        return True
    return False

def play():
    print("Welcome to Tic Tac Toe!\n")
    display_board()

    while True:
        player_input('X')
        display_board()
        if check_win('X'):
            print("Player X has won the game!")
            break

        player_input('O')
        display_board()
        if check_win('O'):
            print("Player O has won the game!")
            break

play()