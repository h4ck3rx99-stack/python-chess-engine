# --- ChessEngine.py ---

class GameState:
    def __init__(self):
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]
        self.white_to_move = True
        self.move_log = []

    def make_move(self, move):
        self.board[move.start_row][move.start_col] = "--"
        self.board[move.end_row][move.end_col] = move.piece_moved
        self.move_log.append(move)
        self.white_to_move = not self.white_to_move

    # --- NEW: MOVE GENERATION SKELETON ---

    def get_valid_moves(self):
        # 1. Get all possible moves.
        # 2. For each move, make it.
        # 3. Check if making that move leaves your King in danger.
        # 4. If it does, it's not a valid move. 
        # (For now, we will just return all possible moves so we can test)
        return self.get_all_possible_moves()

    def get_all_possible_moves(self):
        moves = []
        for r in range(len(self.board)):       # number of rows
            for c in range(len(self.board[r])):    # number of cols in given row
                turn = self.board[r][c][0]     # Gets the color ('w', 'b', or '-')
                
                if (turn == 'w' and self.white_to_move) or (turn == 'b' and not self.white_to_move):
                    piece = self.board[r][c][1]
                    if piece == 'p':
                        self.get_pawn_moves(r, c, moves)
                    # We will add elif statements for 'R', 'N', 'B', 'Q', 'K' later
        return moves

    def get_pawn_moves(self, r, c, moves):
        # White pawns move up the board (decreasing row index)
        if self.white_to_move: 
            if self.board[r-1][c] == "--": # 1 square advance
                moves.append(Move((r, c), (r-1, c), self.board))
                if r == 6 and self.board[r-2][c] == "--": # 2 square advance from start
                    moves.append(Move((r, c), (r-2, c), self.board))
            # Captures to the left and right would go here!
        else:
            # Black pawn logic goes here (increasing row index)
            pass

class Move:
    ranks_to_rows = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}
    files_to_cols = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}

    def __init__(self, start_sq, end_sq, board):
        self.start_row = start_sq[0]
        self.start_col = start_sq[1]
        self.end_row = end_sq[0]
        self.end_col = end_sq[1]
        self.piece_moved = board[self.start_row][self.start_col]
        self.piece_captured = board[self.end_row][self.end_col]