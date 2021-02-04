import sys

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

def Astar(start_state, goal_state, actions_f, take_action_f, h_f):
	h = h_f(start_state)
	g = 0
	start_node = Node(state=start_state, f=(g + h), g=g, h=h)
	expanded = {}
	un_expanded = [start_node]
	came_from = {}

	if (start_state == goal_state):
		return ([start_state], came_from)

	while (len(un_expanded) > 0):
		best_node = un_expanded.pop(0)
		
		children = []
		actions = actions_f(best_node.state)
		for action in actions:
			(child_state, step_cost) = take_action_f(best_node.state, action)
			g = best_node.g + step_cost
			h = h_f(child_state)
			f = g + h
			child_node = Node(state=child_state, f=f, g=g, h=h)
			children.append(child_node)
		
		expanded[tuple(best_node.state)] = best_node
		for child in list(children):
			if tuple(child.state) in expanded:
				if child.f > expanded[tuple(child.state)].f:
					 children.remove(child)
			if tuple(child.state) in un_expanded:
				if child.f > expanded[tuple(child.state)].f:
					 children.remove(child)
		
		c_states = []
		for c in children:
			c_states.append(c.state)
			came_from[tuple(c.state)] = best_node
			
		if (goal_state in c_states):
			solution_path = []
			while (tuple(goal_state) in came_from):
				solution_path.insert(0, goal_state)
				goal_state = came_from[tuple(goal_state)].state
			solution_path.insert(0, start_state)
			return (solution_path, came_from)
			
		for child in children:
			un_expanded.insert(0, child)
		un_expanded = sorted(un_expanded, key = lambda x: x.f)
	
start_state1 = [0, 8, 1, 4, 2, 3, 7, 6, 5]
start_state2 = [4, 2, 5, 1, 3, 6, 0, 7, 8]
start_state3 = [2, 4, 3, 8, 0, 5, 7, 6, 1]
start_state4 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
solution_path = []
tree = {}

solution_path, tree = Astar(start_state4, goal_state, actions_8p, take_action_8p, lambda s: h_manhattan_sum(s, goal_state))
print(solution_path)
print(len(tree))

			
			
