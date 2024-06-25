import os

board = [" " for _ in range(10)]

def print_game_header():
    print("WELCOME TO TIC-TAC-TOE")

def print_board():
    print("     |     |     ")
    print("  " + board[1] + "  |  " + board[2] + "  |  " + board[3] + "  ")
    print("     |     |     ")
    print("-----|-----|-----")
    print("     |     |     ")
    print("  " + board[4] + "  |  " + board[5] + "  |  " + board[6] + "  ")
    print("     |     |     ")
    print("-----|-----|-----")
    print("     |     |     ")
    print("  " + board[7] + "  |  " + board[8] + "  |  " + board[9] + "  ")
    print("     |     |     ")

def is_winner(board_state, player_marker):
    return ((board_state[1] == player_marker and board_state[2] == player_marker and board_state[3] == player_marker) or
            (board_state[4] == player_marker and board_state[5] == player_marker and board_state[6] == player_marker) or
            (board_state[7] == player_marker and board_state[8] == player_marker and board_state[9] == player_marker) or
            (board_state[1] == player_marker and board_state[4] == player_marker and board_state[7] == player_marker) or
            (board_state[2] == player_marker and board_state[5] == player_marker and board_state[8] == player_marker) or
            (board_state[3] == player_marker and board_state[6] == player_marker and board_state[9] == player_marker) or
            (board_state[1] == player_marker and board_state[5] == player_marker and board_state[9] == player_marker) or
            (board_state[3] == player_marker and board_state[5] == player_marker and board_state[7] == player_marker))

def is_board_full(board_state):
    return " " not in board_state[1:]

def player_move(player_marker):
    while True:
        try:
            choice = int(input(f"Player {player_marker}, choose an empty square (1-9): "))
            if choice >= 1 and choice <= 9:
                if board[choice] == " ":
                    board[choice] = player_marker
                    break
                else:
                    print("This square has already been chosen! Try another square.")
            else:
                print("Invalid input! Choose a number between 1 and 9.")
        except ValueError:
            print("Invalid input! Please enter a number.")

while True:
    os.system("clear")
    print_game_header()
    print_board()
    
    # Player X move
    player_move("X")
    if is_winner(board, "X"):
        os.system("clear")
        print_game_header()
        print_board()
        print("Player X wins! Congratulations!")
        break
    elif is_board_full(board):
        os.system("clear")
        print_game_header()
        print_board()
        print("It's a tie!")
        break
    
    os.system("clear")
    print_game_header()
    print_board()

    # Player O move
    player_move("O")
    if is_winner(board, "O"):
        os.system("clear")
        print_game_header()
        print_board()
        print("Player O wins! Congratulations!")
        break
    elif is_board_full(board):
        os.system("clear")
        print_game_header()
        print_board()
        print("It's a tie!")
        break
