import sys
from SearchAlgorithms import RBFS, iterative_deepening_search, depth_limited_search, Astar

from GameLogic import find_blank_8p
from GameLogic import goal_test
from GameLogic import actions_8p
from GameLogic import take_action_8p

from heuristics import h_manhattan_sum

start_state1 = [0, 8, 1, 4, 2, 3, 7, 6, 5]
start_state2 = [4, 2, 5, 1, 3, 6, 0, 7, 8]
start_state3 = [2, 4, 3, 8, 0, 5, 7, 6, 1]
start_state4 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
start_state5 = [2, 0, 3, 1, 5, 6, 4, 7, 8]
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
'''
RBFS_result, depth  = RBFS(start_state3, actions_8p, take_action_8p,
                        lambda s: goal_test(s, goal_state),
                        lambda s: h_manhattan_sum(s, goal_state))
'''

#IDS_result = iterative_deepening_search(start_state1, goal_state, actions_8p, take_action_8p, 30)

#DLS_result = depth_limited_search(start_state1, goal_state, actions_8p, take_action_8p, 15)

Astar_result, depth = Astar(start_state3, goal_state, actions_8p, take_action_8p, lambda s: h_manhattan_sum(s, goal_state))
print(Astar_result)
print('\n')
print(depth)
				
