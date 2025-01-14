#!/usr/bin/python3
def print_board(board):
    """
    Prints the current state of the board.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * (len(row) * 4 - 1))  # Adjust separator length dynamically

def check_winner(board):
    """
    Checks if there is a winner on the board.

    Returns:
        True if a player has won, False otherwise.
    """
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]  # Return the winner ('X' or 'O')

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None  # No winner yet

def is_draw(board):
    """
    Checks if the board is full and there is no winner.

    Returns:
        True if the game is a draw, False otherwise.
    """
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """
    Main function to run the Tic-Tac-Toe game.
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    
    while True:
        print_board(board)
        print(f"Player {player}'s turn.")
        
        # Input validation
        try:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid input. Please enter numbers between 0 and 2.")
                continue
        except ValueError:
            print("Invalid input. Please enter valid integers.")
            continue
        
        # Check if the selected cell is empty
        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue
        
        # Make the move
        board[row][col] = player
        
        # Check for a winner
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break
        
        # Check for a draw
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # Switch player
        player = "O" if player == "X" else "X"

# Run the game
if __name__ == "__main__":
    tic_tac_toe()
