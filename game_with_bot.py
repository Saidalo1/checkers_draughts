from draughts import Board, Move
from draughts.engine import Limit
from draughts.engines.hub import HubEngine


def main():
    board = Board(variant="russian")

    # engine = HubEngine(["scan-master/scan_linux", "scan-master/scan.ini"])
    engine = HubEngine(["Engines/Russian/Analytic.eng", "Engines/Russian/Analytic.evf"])

    print("Welcome to the Russian checkers game!")
    print("Enter moves in the format: starting_position-ending_position (for example, '9, 13')")
    print("Use 'q' to quit the game.")

    while True:
        print(board)
        possible_moves = list(map(lambda i: i.steps_move, board.legal_moves()))
        print("Legal moves:", possible_moves)

        move_str = input("Your move: ").strip()

        if move_str.lower() == 'q':
            print("Game over.")
            break

        moves = list(map(int, move_str.split(', ')))
        player_move = Move(board, steps_move=moves)

        if player_move.steps_move in possible_moves:
            board.push(player_move)
        else:
            print("Invalid move. Please try again.")
            continue

        limit = Limit(time=10)
        engine_move = engine.play(board, limit, False)
        if engine_move.move:
            board.push(engine_move.move)
        else:
            print("Bot cannot make a move.")

    print("Game over.")


if __name__ == "__main__":
    main()
