"""
main.py – Entry point. Handles menus, game loop, and player turns.

Run:
    python main.py
"""
import sys
import io
# Force UTF-8 output on Windows so Unicode characters print correctly
if sys.stdout.encoding != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

import os
import time
from game import (
    make_board, display_board, check_winner, is_draw,
    available_moves, best_ai_move,
    colour, BOLD, RESET, GREEN, YELLOW, RED, CYAN,
)
from scores import load_scores, save_scores, display_scores


# ── Helpers ───────────────────────────────────────────────────────────────────

def clear() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def banner() -> None:
    clear()
    print(colour("""
  +=========================+
  |   >>  TIC  TAC  TOE  << |
  +=========================+
""", BOLD + CYAN))


def get_player_move(board: list[str], player: str, mark: str) -> int:
    """Prompt a human player and validate their input."""
    mark_colour = RED if mark == "X" else CYAN
    while True:
        try:
            raw = input(f"  {BOLD}{colour(player, mark_colour)} ({mark}){RESET} → Enter cell [1-9]: ")
            idx = int(raw.strip()) - 1
            if idx in available_moves(board):
                return idx
            else:
                print(colour("  ⚠  That cell is taken or invalid. Try again.", YELLOW))
        except (ValueError, KeyboardInterrupt):
            print(colour("  ⚠  Enter a number between 1 and 9.", YELLOW))


# ── Game modes ────────────────────────────────────────────────────────────────

def play_vs_computer(scores: dict) -> None:
    """Human (X) vs Computer (O)."""
    board = make_board()
    human, ai = "X", "O"
    current = human  # human goes first

    while True:
        banner()
        display_board(board)

        if current == human:
            idx = get_player_move(board, "Player 1", human)
            board[idx] = human
        else:
            print(f"  {BOLD}{colour('Computer', CYAN)}{RESET} is thinking…")
            time.sleep(0.6)
            idx = best_ai_move(board, ai, human)
            board[idx] = ai

        winner = check_winner(board)
        if winner:
            banner()
            display_board(board)
            if winner == human:
                print(colour("  🎉 You win! Congrats!", GREEN + BOLD))
                scores["Player 1"] += 1
            else:
                print(colour("  🤖 Computer wins! Better luck next time.", RED + BOLD))
                scores["Computer"] += 1
            save_scores(scores)
            return

        if is_draw(board):
            banner()
            display_board(board)
            print(colour("  🤝 It's a draw!", YELLOW + BOLD))
            scores["Draws"] += 1
            save_scores(scores)
            return

        current = ai if current == human else human


def play_two_players(scores: dict) -> None:
    """Player 1 (X) vs Player 2 (O)."""
    board = make_board()
    players = [("Player 1", "X"), ("Player 2", "O")]
    turn = 0

    while True:
        player_name, mark = players[turn % 2]
        banner()
        display_board(board)
        idx = get_player_move(board, player_name, mark)
        board[idx] = mark

        winner = check_winner(board)
        if winner:
            banner()
            display_board(board)
            print(colour(f"  🎉 {player_name} wins!", GREEN + BOLD))
            scores[player_name] += 1
            save_scores(scores)
            return

        if is_draw(board):
            banner()
            display_board(board)
            print(colour("  🤝 It's a draw!", YELLOW + BOLD))
            scores["Draws"] += 1
            save_scores(scores)
            return

        turn += 1


# ── Main menu ─────────────────────────────────────────────────────────────────

def main() -> None:
    scores = load_scores()

    while True:
        banner()
        display_scores(scores, colour)
        print(f"  {BOLD}Main Menu{RESET}")
        print(f"  {CYAN}1.{RESET} Play vs Computer")
        print(f"  {CYAN}2.{RESET} 2-Player Mode")
        print(f"  {CYAN}3.{RESET} Reset Scores")
        print(f"  {CYAN}4.{RESET} Quit")
        print()

        choice = input("  Choose [1-4]: ").strip()

        if choice == "1":
            play_vs_computer(scores)
            _ask_play_again()
        elif choice == "2":
            play_two_players(scores)
            _ask_play_again()
        elif choice == "3":
            scores = {"Player 1": 0, "Player 2": 0, "Computer": 0, "Draws": 0}
            save_scores(scores)
            print(colour("  ✅ Scores reset!", GREEN))
            time.sleep(1)
        elif choice == "4":
            print(colour("\n  👋 Thanks for playing! Bye!\n", CYAN))
            break
        else:
            print(colour("  ⚠  Invalid choice.", YELLOW))
            time.sleep(0.8)


def _ask_play_again() -> None:
    print()
    input("  Press Enter to return to the menu…")


if __name__ == "__main__":
    main()
