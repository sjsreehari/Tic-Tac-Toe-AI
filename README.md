# Unbeatable Tic Tac Toe AI

A Python implementation of Tic Tac Toe using the **Minimax algorithm** — no external ML frameworks required.

Made while learning **AI concepts from Harvard’s CS50 Introduction to AI with Python**.

---

## Overview

This project demonstrates how to build a fully functional **game-playing AI** from scratch in a single file. It includes:

* **Terminal Version** – play directly in the console.
* **GUI Version** – play with a Tkinter interface.
* **Minimax Algorithm** – AI evaluates all possible moves to guarantee optimal play.
* **Modular Logic in One File** – easy to read, modify, and extend.

This is perfect for beginners who want to understand **adversarial search, game AI, and Python GUI integration**.

---

## Features

* AI never loses in Tic Tac Toe.
* Terminal and GUI versions included.
* Clean, modular code in a single Python file:

  * Switch between terminal and GUI play.
  * Experiment with move-ordering or Alpha-Beta Pruning.
* Easy to read, understand, and reuse for other games.

---

## Key Learnings

* How **Minimax** works in adversarial games.
* How the AI simulates all possible moves to guarantee optimal play.
* Why larger games (like Chess ≈10^120 states) require **Alpha-Beta Pruning** and heuristics.
* How to integrate algorithmic logic with **Python GUI**.

---

## Getting Started

Clone the repository:

```bash
git clone https://github.com/sjsreehari/tic-tac-toe-minimax-ai.git
cd tic-tac-toe-minimax-ai
```

(Optional) Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

* **Windows (PowerShell):** `.\venv\Scripts\Activate.ps1`
* **Windows (CMD):** `.\venv\Scripts\activate`
* **macOS / Linux:** `source venv/bin/activate`

Run the terminal version:

```bash
python tictactoe.py
```

Run the GUI version:

```bash
python tictactoe.py gui
```

---


## Future Improvements

* Implement **Alpha-Beta Pruning** for efficiency.
* Extend to other board games (4x4, Connect Four).
* Add difficulty levels or heuristic-based AI for larger games.
* Improve GUI with animations and better UX.

---

## Author

Developed by [Sreehari S J](https://www.linkedin.com/in/sreeharisj/)

---
