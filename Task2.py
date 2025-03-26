import math

# Tic-Tac-Toe Board
board = [' ' for _ in range(9)]
def print_board():
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("--+---+--")

def check_winner(board, player):
    win_combos = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
                  (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
                  (0, 4, 8), (2, 4, 6)]             # Diagonals
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_combos)

def is_full(board):
    return ' ' not in board

def minimax(board, depth, is_maximizing, alpha, beta):
    if check_winner(board, 'O'):
        return 1
    if check_winner(board, 'X'):
        return -1
    if is_full(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, False, alpha, beta)
                board[i] = ' '
                max_eval = max(max_eval, score)
                alpha = max(alpha, score)
                if beta <= alpha:
                    break  
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, True, alpha, beta)
                board[i] = ' '
                min_eval = min(min_eval, score)
                beta = min(beta, score)
                if beta <= alpha:
                    break  # Alpha-Beta Pruning
        return min_eval

# AI's best move
def best_move():
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False, -math.inf, math.inf)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

# Main Game Loop
def play_game():
    print("Welcome to Tic-Tac-Toe! You're 'X', and AI is 'O'.")
    print_board()

    while True:
        # Human Move
        try:
            human_move = int(input("Enter your move (1-9): ")) - 1
            if board[human_move] != ' ':
                print("Invalid move. Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Enter a number between 1-9.")
            continue
        
        board[human_move] = 'X'
        print_board()

        if check_winner(board, 'X'):
            print("🎯 You win! Congratulations!")
            break
        if is_full(board):
            print("🤝 It's a draw!")
            break
        
        ai_move = best_move()
        board[ai_move] = 'O'
        print("\nAI plays:")
        print_board()

        if check_winner(board, 'O'):
            print("🤖 AI wins! Better luck next time.")
            break
        if is_full(board):
            print("🤝 It's a draw!")
            break

play_game()
