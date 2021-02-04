from queue import PriorityQueue

from GameLogic import find_blank_8p
from GameLogic import goal_test
from GameLogic import actions_8p
from GameLogic import take_action_8p

from heuristics import h_manhattan_sum
from heuristics import h_hamming

class Node:
    def __init__(self, state, f=0, g=0, h=0):
        self.state = state
        self.f = f
        self.g = g
        self.h = h
    def __repr__(self):
        return f'Node({self.state}, f={self.f}, g={self.g}, h={self.h})'

def greedy_best_first(start_state, goal_state, actions_f, take_action_f, h_f):
	h = h_f(start_state)
	g = 0
	start_node = Node(state=start_state, f=h, g=g, h=h)
	search_queue = [start_node]
	
	while (search_queue):
		#search_queue = sorted(search_queue, key = lambda x: x.h)
		
		current_node = search_queue.pop(0)
		current_state = current_node.state
		current_heuristic = current_node.h
		starting_counter = current_node.g
		actions = actions_f(current_state)
		
		print(current_node)
		for action in actions:
			current_action = action
			(successor_state, step_cost) = take_action_f(current_state, current_action)
			
			if successor_state == goal_state:
				return 'arrived!'
			
			successor_heuristic = h_f(successor_state)
			successor_node = Node(state=successor_state, h=successor_heuristic)
			current_node = Node(state=current_state, h=current_heuristic)
			
			if successor_heuristic < current_heuristic:
				search_queue.insert(0, current_node)
				search_queue.insert(0, successor_node)
				break
			else:
				search_queue.append(successor_node)
	return 'no plan found'
	
start_state1 = [0, 8, 1, 4, 2, 3, 7, 6, 5]
start_state2 = [4, 2, 5, 1, 3, 6, 0, 7, 8]
start_state3 = [2, 4, 3, 8, 0, 5, 7, 6, 1]
start_state4 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
start_state5 = [1, 2, 3, 4, 5, 6, 0, 7, 8]
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
solution_path = []

solution = greedy_best_first(start_state4, goal_state, actions_8p, take_action_8p, lambda s: h_manhattan_sum(s, goal_state))
print(solution)
		
		
				
