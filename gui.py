import tkinter as tk
from tkinter import messagebox
from game import make_board, check_winner, is_draw, best_ai_move, available_moves
import random

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("350x450")
        self.root.configure(bg="#2b2b2b")

        self.board = make_board()
        self.human_mark = "X"
        self.ai_mark = "O"
        self.current_turn = "X"
        self.mode = "AI" # Can be "AI" or "2P"

        self.scores = {"Player 1 (X)": 0, "Player 2 (O)": 0, "Computer (O)": 0, "Draws": 0}

        self.setup_ui()

    def setup_ui(self):
        # Top Frame for Mode Selection
        top_frame = tk.Frame(self.root, bg="#2b2b2b")
        top_frame.pack(pady=10)

        self.mode_var = tk.StringVar(value="AI")
        tk.Radiobutton(top_frame, text="vs Computer", variable=self.mode_var, value="AI", command=self.reset_game, bg="#2b2b2b", fg="white", selectcolor="#444").pack(side=tk.LEFT, padx=10)
        tk.Radiobutton(top_frame, text="2 Player", variable=self.mode_var, value="2P", command=self.reset_game, bg="#2b2b2b", fg="white", selectcolor="#444").pack(side=tk.LEFT, padx=10)

        # Score Label
        self.score_label = tk.Label(self.root, text=self.get_score_text(), bg="#2b2b2b", fg="white", font=("Arial", 12))
        self.score_label.pack(pady=5)

        # Game Grid
        grid_frame = tk.Frame(self.root, bg="black")
        grid_frame.pack(pady=10)

        self.buttons = []
        for i in range(9):
            btn = tk.Button(grid_frame, text="", font=("Arial", 36, "bold"), width=3, height=1,
                            bg="#3b3b3b", fg="white", activebackground="#4b4b4b",
                            command=lambda idx=i: self.on_click(idx))
            row, col = divmod(i, 3)
            btn.grid(row=row, column=col, padx=2, pady=2)
            self.buttons.append(btn)

        # Reset Button
        tk.Button(self.root, text="Restart Game", font=("Arial", 12), command=self.reset_game, bg="#5c5c5c", fg="white").pack(pady=10)

    def get_score_text(self):
        if self.mode_var.get() == "AI":
            return f"You: {self.scores['Player 1 (X)']}  |  Comp: {self.scores['Computer (O)']}  |  Draws: {self.scores['Draws']}"
        else:
            return f"P1(X): {self.scores['Player 1 (X)']}  |  P2(O): {self.scores['Player 2 (O)']}  |  Draws: {self.scores['Draws']}"

    def update_score_label(self):
        self.score_label.config(text=self.get_score_text())

    def on_click(self, idx):
        if str(idx + 1) not in self.board:
            return # Cell already taken

        # Make Move
        self.make_move(idx, self.current_turn)

        if self.check_game_over():
            return

        # Next turn logic
        if self.mode_var.get() == "AI":
            if self.current_turn == self.human_mark:
                # Switch to AI
                self.current_turn = self.ai_mark
                self.root.after(500, self.ai_turn) # slight delay for realism
        else:
            # 2 Player mode, just switch turns
            self.current_turn = "O" if self.current_turn == "X" else "X"

    def make_move(self, idx, mark):
        self.board[idx] = mark
        color = "#ff5555" if mark == "X" else "#55ffff"
        self.buttons[idx].config(text=mark, fg=color)

    def ai_turn(self):
        if not available_moves(self.board):
            return

        best_idx = best_ai_move(self.board, self.ai_mark, self.human_mark)
        self.make_move(best_idx, self.ai_mark)
        
        if not self.check_game_over():
            self.current_turn = self.human_mark

    def check_game_over(self):
        winner = check_winner(self.board)
        if winner:
            self.handle_win(winner)
            return True
        elif is_draw(self.board):
            self.handle_draw()
            return True
        return False

    def handle_win(self, winner):
        if self.mode_var.get() == "AI":
            if winner == self.human_mark:
                self.scores['Player 1 (X)'] += 1
                messagebox.showinfo("Game Over", "🎉 You win!")
            else:
                self.scores['Computer (O)'] += 1
                messagebox.showinfo("Game Over", "🤖 Computer wins!")
        else:
            if winner == "X":
                self.scores['Player 1 (X)'] += 1
            else:
                self.scores['Player 2 (O)'] += 1
            messagebox.showinfo("Game Over", f"🎉 Player {winner} wins!")
        
        self.update_score_label()
        self.disable_buttons()

    def handle_draw(self):
        self.scores['Draws'] += 1
        self.update_score_label()
        messagebox.showinfo("Game Over", "🤝 It's a draw!")
        self.disable_buttons()

    def disable_buttons(self):
        for btn in self.buttons:
            btn.config(state=tk.DISABLED)

    def reset_game(self):
        self.board = make_board()
        self.current_turn = "X"
        for btn in self.buttons:
            btn.config(text="", state=tk.NORMAL)
        self.update_score_label()

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeGUI(root)
    root.mainloop()
