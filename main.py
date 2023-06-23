from code.classes.board import Board
from code.algorithms.random import Random
from code.visualization.color_blocks import visualize_board
from code.algorithms.breadth_first import BreadthFirst
from code.algorithms.depth_first import DepthFirst
from code.algorithms.astar import AStar
from code.algorithms.hillclimber import HillClimber
from experiment import start_time, end_time

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
    # Start timer
    
    
    for i in range(amount_of_times):
# -------------------------------------- Random search ------------------------------------------------------------------------------
        if algorithm == 'random':
            start_time()
            random = Random(board)
            random.go()
            i += 1
            end_time(start_time)
# ------------------------------------- Breadth-first search ------------------------------------------------------------------------
        elif algorithm == 'bf':
            start_time()
            breadth_first = BreadthFirst(board)
            breadth_first.go()
            i += 1
            end_time(start_time)
# -------------------------------------- Depth-first search ------------------------------------------------------------------------
        elif algorithm == 'df':
            start_time()
            depth_first = DepthFirst(board)
            depth_first.go()
            i += 1
            end_time(start_time)
# ------------------------------------------ A* search ------------------------------------------------------------------------
        elif algorithm == 'astar':
            start_time()
            astar = AStar(board) 
            astar.go()
            i += 1
            end_time(start_time)
# -------------------------------------- Hill Climber search ------------------------------------------------------------------------
        elif algorithm == 'hillclimber':
            start_time()
            random = Random(board)
            random_solution = random.go()
            solution = random_solution.directions

            hill_climber = HillClimber(random_solution, board, solution)
            hill_climber.go(500)
            i += 1
            end_time(start_time)