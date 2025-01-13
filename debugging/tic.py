#!/usr/bin/python3

def print_board(board):
    """Prints the current game board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """Checks if there is a winner."""
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    """Main function for the Tic-Tac-Toe game."""
    board = [[" "]*3 for _ in range(3)]  # Initialize the 3x3 board
    player = "X"  # Player X always starts

    while True:
        print_board(board)

        # Get row input and ensure it's valid
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
        except ValueError:
            print("Invalid input. Please enter integers only.")
            continue
        
        # Check if the input is within bounds
        if row not in [0, 1, 2] or col not in [0, 1, 2]:
            print("Invalid row or column. Please enter values between 0 and 2.")
            continue

        # Check if the spot is available
        if board[row][col] == " ":
            board[row][col] = player
            if check_winner(board):
                print_board(board)
                print("Player " + player + " wins!")
                break  # End the game when there's a winner
            # Switch player
            player = "O" if player == "X" else "X"
        else:
            print("That spot is already taken! Try again.")

# Start the game
tic_tac_toe()
