from code.classes.board import Board
from code.algorithms.random import Random
from code.visualization.color_blocks import visualize_board
from code.algorithms.breadth_first import BreadthFirst
from code.algorithms.depth_first import DepthFirst
from code.algorithms.astar import AStar
from code.algorithms.hillclimber import HillClimber
from experiment import start_time, end_time, output_experiment

from sys import argv
import time



if __name__ == "__main__":
    if len(argv) < 2:
        # Raise error if game name is not given
        print("Usage: python main.py [game] [algorithm]")
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
    
    for i in range(amount_of_times):
# -------------------------------------- Random search ------------------------------------------------------------------------------
        if algorithm == 'random':
            start = start_time()
            random = Random(board)
            random.go()
            elapsed_time = end_time(start)

            # output
            n = i + 1
            game = game_name
            algorithm = algorithm
            dimension = board.dim
            time = elapsed_time
            won = 1

            number_of_moves, number_of_states, solution = random.generate_output()
            print(f"number of moves: {number_of_moves}")
            print(f"number of states: {number_of_states}")
            print(f"solution: {solution}")
            output_experiment(n, game, algorithm, dimension, time, number_of_moves, number_of_states, won, solution)

            i += 1

# ------------------------------------- Breadth-first search ------------------------------------------------------------------------
        elif algorithm == 'breadthfirst':
            start = start_time()
            breadth_first = BreadthFirst(board)
            breadth_first.go()
            elapsed_time = end_time(start)

            # output
            n = i + 1
            game = game_name
            algorithm = algorithm
            dimension = board.dim
            time = elapsed_time
            won = 1

            number_of_moves, number_of_states, solution = breadth_first.generate_output()
            print(f"number of moves: {number_of_moves}")
            print(f"number of states: {number_of_states}")
            print(f"solution: {solution}")
            # output_experiment(n, game, algorithm, dimension, time, number_of_moves, number_of_states, won, solution)

            i += 1
# -------------------------------------- Depth-first search ------------------------------------------------------------------------
        elif algorithm == 'depthfirst':
            start = start_time()
            depth_first = DepthFirst(board)
            depth_first.go()
            elapsed_time = end_time(start)

            # output
            n = i + 1
            game = game_name
            algorithm = algorithm
            dimension = board.dim
            time = elapsed_time
            won = 1

            number_of_moves, number_of_states, solution = depth_first.generate_output()
            print(f"number of moves: {number_of_moves}")
            print(f"number of states: {number_of_states}")
            print(f"solution: {solution}")
            output_experiment(n, game, algorithm, dimension, time, number_of_moves, number_of_states, won, solution)

            i += 1
# ------------------------------------------ A* search ------------------------------------------------------------------------
        elif algorithm == 'astar':
            start = start_time()
            astar = AStar(board) 
            astar.go()
            elapsed_time = end_time(start)

            # output
            n = i + 1
            game = game_name
            algorithm = algorithm
            dimension = board.dim
            time = elapsed_time
            won = 1

            number_of_moves, number_of_states, solution = astar.generate_output()
            print(f"number of moves: {number_of_moves}")
            print(f"number of states: {number_of_states}")
            print(f"solution: {solution}")
            output_experiment(n, game, algorithm, dimension, time, number_of_moves, number_of_states, won, solution)

            i += 1
# -------------------------------------- Hill Climber search ------------------------------------------------------------------------
        elif algorithm == 'hillclimber':
            start = start_time()
            hill_climber = HillClimber(board)
            hill_climber.run_iterations(2)
            elapsed_time = end_time(start)

            # output
            n = i + 1
            game = game_name
            algorithm = algorithm
            dimension = board.dim
            time = elapsed_time
            won = 1

            number_of_moves, number_of_states, solution, state_space = hill_climber.generate_output()
            print(f"number of moves: {number_of_moves}")
            print(f"number of states: {number_of_states}")
            print(f"solution: {solution}")
            print(f"state space: {state_space}")
            # output_experiment(n, game, algorithm, dimension, time, number_of_moves, number_of_states, won, solution, state_space)

            i += 1