import sys
from SearchAlgorithms import RBFS, iterative_deepening_search, depth_limited_search, Astar

from branching import effective_branching_factor

from GameLogic import find_blank_8p
from GameLogic import goal_test
from GameLogic import actions_8p
from GameLogic import take_action_8p

from heuristics import h_manhattan_sum, h_hamming

start_state1 = [0, 8, 1, 4, 2, 3, 7, 6, 5]
start_state2 = [4, 2, 5, 1, 3, 6, 0, 7, 8]
start_state3 = [2, 4, 3, 8, 0, 5, 7, 6, 1]
start_state4 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
start_state5 = [2, 0, 3, 1, 5, 6, 4, 7, 8]
start_state6 = [1, 2, 5, 3, 4, 0, 6, 7, 8]
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
goal_state2 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
node_count = 0
'''
RBFS_result, depth, node_count  = RBFS(start_state3, actions_8p, take_action_8p,
							lambda s: goal_test(s, goal_state),
							lambda s: h_manhattan_sum(s, goal_state))
'''
#IDS_result, node_count = iterative_deepening_search(start_state1, goal_state, actions_8p, take_action_8p, 30)

#DLS_result, node_count = depth_limited_search(start_state6, goal_state2, actions_8p, take_action_8p, 15, node_count)

Astar_result, depth, node_count = Astar(start_state4, goal_state, actions_8p, take_action_8p, lambda s: h_manhattan_sum(s, goal_state))

print(Astar_result)
print('\n')
print(node_count)
print('\n')
print(effective_branching_factor(node_count, len(Astar_result) - 1))
print('\n')
    
def transform_to_flat(solution):
	path = []
	solution_tree = {}
	solution_tree['name'] = solution[0]
	solution_tree['parent'] = "null"
	path.append(solution_tree)
	i = 1
	
	while (i < len(solution)):
		child = {}
		child['name'] = solution[i]
		child['parent'] = solution[i - 1]
		path.append(child)
		i += 1
		
	return path

print(transform_to_flat(Astar_result))
	

				
