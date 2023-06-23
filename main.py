from code.classes.board import Board
from code.algorithms.random import Random
from code.visualization.color_blocks import visualize_board
from code.algorithms.breadth_first import BreadthFirst
from code.algorithms.depth_first import DepthFirst
from code.algorithms.astar import AStar
from code.algorithms.hillclimber import HillClimber
from code.algorithms.iterativedeepening import IterativeDeepening

from sys import argv
import time


if __name__ == "__main__":
    if len(argv) < 2:
        # Raise error if game name is not given
        print("Usage: python main.py [game] [optional: [algorithm]]")
        exit(1)
    elif len(argv) == 2:
        algorithm = 'random'
    elif len(argv) == 3:
        algorithm = argv[2]

    # Extract command line argument
    game_name = argv[1]
    # Initialize game
    board = Board(game_name)
    # Start timer
    start_time = time.time()
# -------------------------------------- Random search ------------------------------------------------------------------------------
    if algorithm == 'random':
        random = Random(board)
        random.go()     
# ------------------------------------- Breadth-first search ------------------------------------------------------------------------
    elif algorithm == 'bf':
        breadth_first = BreadthFirst(board)
        breadth_first.go()
# -------------------------------------- Depth-first search ------------------------------------------------------------------------
    elif algorithm == 'df':
        depth_first = DepthFirst(board)
        depth_first.go()
# ------------------------------------------ A* search ------------------------------------------------------------------------
    elif algorithm == 'astar':
        astar = AStar(board) 
        astar.go()
# -------------------------------------- Hill Climber search ------------------------------------------------------------------------
    elif algorithm == 'hillclimber':
        hill_climber = HillClimber(board)
        hill_climber.generate_random_solutions(3)
        hill_climber.go()
    elif algorithm == 'test':
        random = Random(board)
        random_solution = random.go()
        solution = random_solution.directions
        random_solution.use_solution(board, solution)
    # ----------------------------------- Iterative Deepening  ------------------------------------------------------------------------
    elif algorithm == 'iterative':
        iterative = IterativeDeepening(board)
        iterative.go()

        

    end_time = time.time()
    elapsed_time = round((end_time - start_time), 4)
    print(f"Puzzle was solved in {elapsed_time}s.")
