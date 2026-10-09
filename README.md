# Python Chess Engine

A minimal, dependency-free chess engine and text-based game loop written in pure Python. Built as a learning project to explore board representation, move generation, and game-state management from scratch.

## Features

- **8×8 board model** using a simple list-of-lists representation (`"wR"`, `"bp"`, `"--"`, etc.).
- **Game state tracking** — piece placement, side to move, and a full move log.
- **Move application** via a `Move` object with start/end coordinates.
- **Text-based play loop** in the terminal — enter moves as raw `row col row col` coordinates.
- **Move-generation skeleton** (`get_valid_moves`) ready to be extended with full legality checks (check detection, castling, en passant, promotion).

## Files

| File | Purpose |
| --- | --- |
| `ChessEngine.py` | Core logic: `GameState`, `Move`, board setup, and move generation. |
| `ChessMain.py` | Terminal driver: prints the board and reads moves from the user. |

## Requirements

- Python 3.8+ (standard library only — no external packages).

## Running

```bash
python ChessMain.py
```

You'll see the starting position printed to the console. Enter a move as four space-separated numbers — `start_row start_col end_row end_col` — where rows and columns are `0`–`7` indexed from the top-left (Black's back rank).

Example — move the white pawn from e2 to e4:

```
Enter move (start_row start_col end_row end_col) or 'q' to quit: 6 4 4 4
```

Type `q` to quit.

> **Note:** Move legality is not yet enforced — `get_valid_moves` is a skeleton. Any syntactically valid move is currently applied. Full validation (leaving your own king in check, special moves) is the next step.

## Roadmap

- [ ] Complete `get_valid_moves` with per-piece movement rules.
- [ ] King-safety / check detection.
- [ ] Castling, en passant, and pawn promotion.
- [ ] Algebraic notation input (`e2e4`) instead of raw coordinates.
- [ ] A simple search-based opponent (minimax + alpha-beta).
