from code.classes.board import Board
from code.algorithms.random import Random
from code.visualization.color_blocks import visualize_board
from code.algorithms.breadth_first import BreadthFirst
from code.algorithms.depth_first import DepthFirst
from code.algorithms.hillclimber import HillClimber
from experiment import start_time, end_time, output_experiment
from sys import argv


if __name__ == "__main__":
    if len(argv) < 2:
        # Raise error if game name, algorithm or amount of runs is not given
        print("Usage: python main.py [game] [algorithm] [amount of runs]")
        exit(1)
    elif len(argv) == 3:
        algorithm = argv[2]
    elif len(argv) == 4:
        algorithm = argv[2]
        amount_of_times = int(argv[3])

    # Extract command line argument
    game_name = argv[1]
    # Initialize game
    board = Board(game_name)  
    game = game_name
    dimension = board.dim 
    
    for i in range(amount_of_times):
# -------------------------------------- Random search ------------------------------------------------------------------------------
        if algorithm == 'random':
            start = start_time()
            random = Random(board)
            random.go()
            elapsed_time = end_time(start)

            # Get output
            n = i + 1

            number_of_moves, number_of_states, solution = random.generate_output()
            # General solution (moet ws nog weg)
            solution = [["A", 1]]
            print(f"Number of moves: {number_of_moves}")
            print(f"Number of states: {number_of_states}")
            print(f"Solution: {solution}")
            output_experiment(n, game, algorithm, dimension, elapsed_time, number_of_moves, number_of_states, solution)

            ordered_solution = random.board.order_solution()
            print(f"Ordered solution: {ordered_solution}")
            print(f"Time: {elapsed_time}")

            visualize_board(board.board, board.cars, save_path=f"code/visualization/board_images/board{n}.png")

# ------------------------------------- Breadth-first search ------------------------------------------------------------------------
        elif algorithm == 'breadthfirst':
            start = start_time()
            breadth_first = BreadthFirst(board)
            breadth_first.go()
            elapsed_time = end_time(start)

            # Get output
            n = i + 1

            number_of_moves, number_of_states, solution = breadth_first.generate_output()
            print(f"Number of moves: {number_of_moves}")
            print(f"Number of states: {number_of_states}")
            print(f"Solution: {solution}")
            output_experiment(n, game, algorithm, dimension, elapsed_time, number_of_moves, number_of_states, solution)

# -------------------------------------- Depth-first search ------------------------------------------------------------------------
        elif algorithm == 'depthfirst':
            start = start_time()
            depth_first = DepthFirst(board)
            depth_first.go()
            elapsed_time = end_time(start)

            # Get output
            n = i + 1

            number_of_moves, number_of_states, solution = depth_first.generate_output()
            print(f"Number of moves: {number_of_moves}")
            print(f"Number of states: {number_of_states}")
            print(f"Solution: {solution}")
            output_experiment(n, game, algorithm, dimension, elapsed_time, number_of_moves, number_of_states, solution)

# -------------------------------------- Hill Climber search ------------------------------------------------------------------------
        elif algorithm == 'hillclimber':
            start = start_time()
            hill_climber = HillClimber(board)
            hill_climber.run_iterations()
            elapsed_time = end_time(start)

            # Get output
            n = i + 1

            number_of_moves, number_of_states, solution = hill_climber.generate_output()
            print(f"number of moves: {number_of_moves}")
            print(f"number of states: {number_of_states}")
            print(f"solution: {solution}")
            output_experiment(n, game, algorithm, dimension, elapsed_time, number_of_moves, number_of_states, solution)
