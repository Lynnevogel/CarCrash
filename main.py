from code.classes.board import Board
from code.algorithms.random import Random
from code.visualization.color_blocks import visualize_board
from code.algorithms.breadth_first import breadth_first
from code.algorithms.depth_first import DepthFirst
from code.algorithms.astar import AStar
from code.algorithms.hillclimber import HillClimber

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
        start_state = board
        breadth_first(start_state)
# -------------------------------------- Depth-first search ------------------------------------------------------------------------
    elif algorithm == 'df':
        depth_first = DepthFirst(board)
        depth_first.go()
# ------------------------------------------ A* search ------------------------------------------------------------------------
    elif algorithm == 'astar':
        astar = AStar(board) 
        astar.solve()
# -------------------------------------- Hill Climber search ------------------------------------------------------------------------
    elif algorithm == 'hillclimber':
        random = Random(board)
        random_solution = random.go()
        solution = random_solution.directions

        hill_climber = HillClimber(random_solution, board, solution)
        hill_climber.go(500)
    elif algorithm == 'test':
        random = Random(board)
        random_solution = random.go()
        solution = random_solution.directions
        random_solution.use_solution(board, solution)

        

    end_time = time.time()
    elapsed_time = round((end_time - start_time), 4)
    print(f"Puzzle was solved in {elapsed_time}s.")
