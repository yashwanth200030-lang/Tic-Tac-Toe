"""
scores.py – Persist win/draw/loss scores to a JSON file.
"""

import json
from pathlib import Path

SCORES_FILE = Path(__file__).parent / "scores.json"


def load_scores() -> dict:
    if SCORES_FILE.exists():
        try:
            return json.loads(SCORES_FILE.read_text())
        except json.JSONDecodeError:
            pass
    return {"Player 1": 0, "Player 2": 0, "Computer": 0, "Draws": 0}


def save_scores(scores: dict) -> None:
    SCORES_FILE.write_text(json.dumps(scores, indent=2))


def display_scores(scores: dict, colour_fn) -> None:
    from game import BOLD, GREEN, YELLOW, CYAN, RESET
    print(f"\n{BOLD}{'='*28}{RESET}")
    print(f"  {BOLD}>> Scoreboard{RESET}")
    print(f"{'='*28}")
    for name, score in scores.items():
        bar = "#" * score
        if name == "Draws":
            print(f"  {YELLOW}{name:<12}{RESET} {score:>2}  {YELLOW}{bar}{RESET}")
        elif name == "Computer":
            print(f"  {CYAN}{name:<12}{RESET} {score:>2}  {CYAN}{bar}{RESET}")
        else:
            print(f"  {GREEN}{name:<12}{RESET} {score:>2}  {GREEN}{bar}{RESET}")
    print(f"{BOLD}{'─'*28}{RESET}\n")
