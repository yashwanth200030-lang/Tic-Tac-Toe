# 🎮 Tic Tac Toe — Python Terminal Game

A colorful, feature-rich **Tic Tac Toe** game playable right in your terminal. Built with pure Python — no external dependencies required.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)

---

## ✨ Features

- 🤖 **vs Computer** — Unbeatable AI powered by the **Minimax algorithm**
- 👥 **2-Player Mode** — Play with a friend on the same machine
- 📊 **Score Tracking** — Wins, losses, and draws are saved between sessions
- 🎨 **Colorful UI** — ANSI-colored board and highlighted player marks
- 🔄 **Play Again** — Jump back to the menu without restarting

---

## 📁 Project Structure

```
tic-tac-toe/
├── main.py       # Entry point — menus & game loop
├── game.py       # Board logic, win detection, Minimax AI
├── scores.py     # Score persistence (saved to scores.json)
├── .gitignore
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites
- Python **3.10 or higher**

### Run the game

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/tic-tac-toe.git
cd tic-tac-toe

# Run
python main.py
```

> No `pip install` needed — uses only Python standard library!

---

## 🕹️ How to Play

1. Run `python main.py`
2. Choose a mode from the menu:
   - `1` → Play vs Computer
   - `2` → 2-Player Mode
   - `3` → Reset Scores
   - `4` → Quit
3. Enter a cell number **(1–9)** on your turn:

```
  1 │ 2 │ 3
 ───┼───┼───
  4 │ 5 │ 6
 ───┼───┼───
  7 │ 8 │ 9
```

---

## 🤖 About the AI

The computer uses the **Minimax algorithm** — it plays optimally every time. You can draw against it if you play perfectly, but you cannot beat it!

---

## 📜 License

MIT License — free to use, modify, and share.

---

> Built with ❤️ by [Yashwanth](https://github.com/YOUR_USERNAME)
