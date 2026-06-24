"""
game.py – Core Tic Tac Toe logic (board, win check, AI).
"""

import random

# ── ANSI colours ─────────────────────────────────────────────────────────────
RESET  = "\033[0m"
BOLD   = "\033[1m"
RED    = "\033[91m"
CYAN   = "\033[96m"
YELLOW = "\033[93m"
GREEN  = "\033[92m"
DIM    = "\033[2m"

PLAYER_COLOURS = {"X": RED, "O": CYAN}


def colour(text: str, code: str) -> str:
    return f"{code}{text}{RESET}"


# ── Board helpers ─────────────────────────────────────────────────────────────

def make_board() -> list[str]:
    """Return a fresh 9-cell board numbered 1-9."""
    return [str(i) for i in range(1, 10)]


def display_board(board: list[str]) -> None:
    """Pretty-print the board with grid lines."""
    symbols = []
    for cell in board:
        if cell == "X":
            symbols.append(colour(cell, BOLD + RED))
        elif cell == "O":
            symbols.append(colour(cell, BOLD + CYAN))
        else:
            symbols.append(colour(cell, DIM))

    print()
    print(f"  {symbols[0]} │ {symbols[1]} │ {symbols[2]}")
    print(f" ───┼───┼───")
    print(f"  {symbols[3]} │ {symbols[4]} │ {symbols[5]}")
    print(f" ───┼───┼───")
    print(f"  {symbols[6]} │ {symbols[7]} │ {symbols[8]}")
    print()


WINNING_COMBOS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # cols
    (0, 4, 8), (2, 4, 6),             # diagonals
]


def check_winner(board: list[str]) -> str | None:
    """Return the winning mark ('X' or 'O'), or None."""
    for a, b, c in WINNING_COMBOS:
        if board[a] == board[b] == board[c]:
            return board[a]
    return None


def is_draw(board: list[str]) -> bool:
    return all(cell in ("X", "O") for cell in board)


def available_moves(board: list[str]) -> list[int]:
    return [i for i, cell in enumerate(board) if cell not in ("X", "O")]


# ── AI (minimax) ─────────────────────────────────────────────────────────────

def minimax(board: list[str], is_maximising: bool, ai_mark: str, human_mark: str) -> int:
    winner = check_winner(board)
    if winner == ai_mark:
        return 1
    if winner == human_mark:
        return -1
    if is_draw(board):
        return 0

    moves = available_moves(board)
    if is_maximising:
        best = -10
        for i in moves:
            board[i] = ai_mark
            score = minimax(board, False, ai_mark, human_mark)
            board[i] = str(i + 1)
            best = max(best, score)
        return best
    else:
        best = 10
        for i in moves:
            board[i] = human_mark
            score = minimax(board, True, ai_mark, human_mark)
            board[i] = str(i + 1)
            best = min(best, score)
        return best


def best_ai_move(board: list[str], ai_mark: str, human_mark: str) -> int:
    """Return index of the best move for the AI."""
    moves = available_moves(board)
    best_score = -10
    best_move = random.choice(moves)  # fallback
    for i in moves:
        board[i] = ai_mark
        score = minimax(board, False, ai_mark, human_mark)
        board[i] = str(i + 1)
        if score > best_score:
            best_score = score
            best_move = i
    return best_move
