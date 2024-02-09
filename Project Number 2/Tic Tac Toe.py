# Erum Iqbal And Aisha Essa
# erum.iqbal346@gmail.com
# safiaessa78@gmail.com

# Project: Tic Tac Toe Game

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 9)
def check_winner(board, player):
# Chwck rows, columns and diagonals for a win.
   for r in range(3):
        if all(board[r][c] == player for c in range(3)) or all(board[c][r] == player for c in range(3)):
            return True
        if all(board[r][r] == player for r in range(3)) or all(board[r][2-r] == player for r in range(3)):
            return True
        return False
        
def is_board_full(board):
    return all(board[r][c] != ' ' for r in range(3) for c in range(3))

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X' , 'O']
    turn = 0

    while True:
        print_board(board)
        player = players[turn%2]
       
        try:
            row = int(input(f"player {player}, enter row (0, 1 or 2):"))
            column = int(input(f"player {player}, enter column(0, 1 or 2):"))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if 0 <= row < 3 and 0 <= column < 3 and board[row][column] == ' ':
            board[row][column] = player
            if check_winner(board, player):
                print_board(board)
                print(f"player{player} wins!")
                break
    
        elif is_board_full(board):
                print_board(board)
                print("it's a tie!")
                break
        turn += 1
    else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
     tic_tac_toe()


