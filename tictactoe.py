import tkinter as tk
from tkinter import messagebox
import math
import sys

# Print Board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Check isTerminal Case
def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None

def is_full(board):
    return all(cell != ' ' for row in board for cell in row)

# MiniMax Algorithm
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == 'O':
        return 1
    elif winner == 'X':
        return -1
    elif is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# Terminal Game 
def terminal_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Tic Tac Toe! You are X, AI is O.")
    print_board(board)

    while True:
        # Player move
        while True:
            try:
                move = input("Enter your move (row col): ").split()
                x, y = int(move[0]), int(move[1])
                if board[x][y] == ' ':
                    board[x][y] = 'X'
                    break
                else:
                    print("Cell already taken!")
            except (ValueError, IndexError):
                print("Invalid input. Enter row and col as 0, 1, or 2.")
        print_board(board)
        if check_winner(board):
            print(f"{check_winner(board)} wins!")
            break
        if is_full(board):
            print("It's a draw!")
            break

        # AI move
        ai_move = best_move(board)
        if ai_move:
            board[ai_move[0]][ai_move[1]] = 'O'
            print("AI played:")
            print_board(board)
            if check_winner(board):
                print(f"{check_winner(board)} wins!")
                break
            if is_full(board):
                print("It's a draw!")
                break

# GUI 
class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe - Minimax AI")
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()

        print("Tic Tac Toe! You are X, AI is O.")
        print_board(self.board)

    def create_board(self):
        for i in range(3):
            for j in range(3):
                btn = tk.Button(self.root, text='', font=('Arial', 32), width=3, height=1,
                                command=lambda x=i, y=j: self.player_move(x, y))
                btn.grid(row=i, column=j)
                self.buttons[i][j] = btn

    def player_move(self, x, y):
        if self.board[x][y] == ' ' and not check_winner(self.board):
            self.board[x][y] = 'X'
            self.buttons[x][y].config(text='X', state='disabled')
            print(f"Player move: {x} {y}")
            print_board(self.board)

            winner = check_winner(self.board)
            if winner:
                print(f"{winner} wins!")
                self.end_game(f'{winner} wins!')
                return
            if is_full(self.board):
                print("It's a draw!")
                self.end_game("It's a draw!")
                return
            self.root.after(300, self.ai_move)

    def ai_move(self):
        move = best_move(self.board)
        if move:
            x, y = move
            self.board[x][y] = 'O'
            self.buttons[x][y].config(text='O', state='disabled')
            print(f"AI played: {x} {y}")
            print_board(self.board)

            winner = check_winner(self.board)
            if winner:
                print(f"{winner} wins!")
                self.end_game(f'{winner} wins!')
                return
            if is_full(self.board):
                print("It's a draw!")
                self.end_game("It's a draw!")
                return

    def end_game(self, message):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(state='disabled')
        messagebox.showinfo("Game Over", message)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "gui":
        root = tk.Tk()
        game = TicTacToeGUI(root)
        root.mainloop()
    else:
        terminal_game()
