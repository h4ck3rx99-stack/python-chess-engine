# --- ChessMain.py ---
import ChessEngine

def print_board(board):
    for row in board:
        print(" ".join(row))
    print("-----------------------")

def main():
    gs = ChessEngine.GameState()
    valid_moves = gs.get_valid_moves()
    
    print("Welcome to Python Chess!")
    print_board(gs.board)

    while True:
        # 1. Ask the user for a move
        # (Assuming they type something like "64 44" for e2 to e4)
        move_str = input("Enter move (start_row start_col end_row end_col) or 'q' to quit: ")
        
        if move_str.lower() == 'q':
            break
            
        try:
            # Parse the input numbers
            coords = move_str.split()
            start_sq = (int(coords[0]), int(coords[1]))
            end_sq = (int(coords[2]), int(coords[3]))
            
            # Create a move object
            user_move = ChessEngine.Move(start_sq, end_sq, gs.board)
            
            # NOTE: We aren't checking if it's in valid_moves yet for this simple test,
            # but normally you would check if user_move is in valid_moves here!
            
            gs.make_move(user_move)
            print_board(gs.board)
            
            # Get the new set of valid moves for the next player
            valid_moves = gs.get_valid_moves()
            
        except Exception as e:
            print("Invalid input format. Try again.")

if __name__ == "__main__":
    main()