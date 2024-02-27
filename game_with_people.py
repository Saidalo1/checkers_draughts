from draughts import Board, Move


def main():
    # Create a board for Russian checkers
    board = Board(variant="russian")

    print("Welcome to the Russian checkers game!")
    print("Enter moves in the format: starting_position-ending_position (for example, '9, 13')")
    print("Use 'q' to quit the game.")

    while True:
        print(board)
        possible_moves = list(map(lambda i: i.steps_move, board.legal_moves()))
        print("Legal moves:", possible_moves)
        move_str = input(" ").strip()

        if move_str.lower() == 'q':
            print("Game over.")
            break

        print(f"DEBUG: Received input: '{move_str}'")

        moves = list(map(int, move_str.split(', ')))
        # if moves in possible_moves:
        try:
            board.push(Move(board, steps_move=moves))
        except ValueError:
            print('there is debug')


# 9, 13
# 24, 20
# 11, 14
# 22, 19
# 13, 18
# 20, 16
# 10, 13

if __name__ == "__main__":
    main()
