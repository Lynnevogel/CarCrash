from code.classes.queue import Queue
from code.classes.board import Board
from code.classes.board import Car
import copy



def breadth_first(start_state):
    queue = Queue()
    queue.enqueue(start_state)
    counter = 0
    while queue:
        state = queue.dequeue()
        print(f"type state 1: {type(state)}")
        if state.is_won():
            return True
        elif counter < 5:
            all_cars = state.cars.keys()
            for car in all_cars:
                possible_moves, _ = state.can_move_car(car)
                queue.enqueue(possible_moves)
            print(f"queue: {queue}")
        counter += 1
# start state verkrijgen

# goal state definiëren

# get_next_states aanmaken
        


# depth = 5
# queue = Queue()
# queue.enqueue("")
# while not queue.size == 0:
#     state = queue.front()
#     print(state)
#     if len(state) < depth:
        