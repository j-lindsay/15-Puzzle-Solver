import sys

class Node:
    def __init__(self, state, f=0, g=0, h=0):
        self.state = state
        self.f = f
        self.g = g
        self.h = h
    def __repr__(self):
        return f'Node({self.state}, f={self.f}, g={self.g}, h={self.h})'

# Implemenation of the A* algorithm based on the content of Chapter 3 section 5 of "Artifical Intelligence: A Modern Approach" by Russell and Norvig.
# Passes functions as parameters so we can implement other puzzles while re-using the same implemenation of A*.

def RBFS(start_state, actions_f, take_action_f, goal_test_f, h_f):
	node_count = 0
	h = h_f(start_state)
	g = 0
	start_node = Node(state=start_state, f=(g + h), g=g, h=h)
	return RBFS_helper(start_node, actions_f, take_action_f, goal_test_f, h_f, float('inf'), node_count)

def RBFS_helper(parent_node, actions_f, take_action_f, goal_test_f, h_f, f_max, node_count):
	if goal_test_f(parent_node.state):
		return ([parent_node.state], parent_node.g, node_count)

	actions = actions_f(parent_node.state)
	if not actions:
		return ('failure', float('inf'), node_count)

	children = []
	for action in actions:
		node_count += 1
		(child_state, step_cost) = take_action_f(parent_node.state, action)
		g = parent_node.g + step_cost
		h = h_f(child_state)
		f = max(h + g, parent_node.f)
		child_node = Node(state=child_state, f=f, g=g, h=h)
		children.append(child_node)

	while True:
		children = sorted(children, key = lambda x: x.f) # sort by f value
		best_child = children[0]
		if best_child.f > f_max:
			return ('failure', best_child.f, node_count)
		alternative_f = children[1].f if len(children) > 1 else float('inf')
		result, best_child.f, node_count = RBFS_helper(best_child, actions_f, take_action_f, 
													goal_test_f, h_f, min(f_max,alternative_f), node_count)
		if result != 'failure':                  
			result.insert(0, parent_node.state)    
			return (result, best_child.f, node_count)  

def iterative_deepening_search(start_state, goal_state, actions_f, take_action_f, max_depth):
	for depth in range(max_depth):
		node_count = 0
		result, node_count = depth_limited_search(start_state, goal_state, actions_f, take_action_f, depth, node_count)
		
		if result == 'failure':
			return ('failure', node_count)
		if result != 'cutoff':
			result.insert(0, start_state)
			return (result, node_count)
	return ('cutoff', node_count)

def depth_limited_search(start_state, goal_state, actions_f, take_action_f, depth_limit, node_count):
	if start_state == goal_state:
		return ([], node_count)
	if depth_limit == 0:
		return ('cutoff', node_count)

	cutoff_occurred = False
	for action in actions_f(start_state):
		node_count += 1
		child_state, step_cost = take_action_f(start_state, action)
		result, node_count = depth_limited_search(child_state, goal_state, actions_f, take_action_f, depth_limit - 1, node_count)
		
		if result == 'cutoff':
			cutoff_occurred = True
		elif result != 'failure':
			result.insert(0, child_state)
			return (result, node_count)

	if cutoff_occurred:
		return ('cutoff', node_count)
	else:
		return ('failure', node_count)
		
def Astar(start_state, goal_state, actions_f, take_action_f, h_f):
	node_count = 1
	h = h_f(start_state)
	g = 0
	start_node = Node(state=start_state, f=(g + h), g=g, h=h)
	expanded = {}
	un_expanded = [start_node]
	came_from = {}
	depth = 0

	if (start_state == goal_state):
		return (start_state, depth, node_count)

	while (len(un_expanded) > 0):
		best_node = un_expanded.pop(0)
		
		children = []
		actions = actions_f(best_node.state)
		for action in actions:
			node_count += 1
			(child_state, step_cost) = take_action_f(best_node.state, action)
			g = best_node.g + step_cost
			h = h_f(child_state)
			f = g + h
			child_node = Node(state=child_state, f=f, g=g, h=h)
			children.append(child_node)
			depth = f
		
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
			came_from[tuple(c.state)] = best_node.state		
		
		if (goal_state in c_states):
			solution_path = []
			while (tuple(goal_state) in came_from):
				solution_path.insert(0, goal_state)
				goal_state = came_from[tuple(goal_state)]
			solution_path.insert(0, start_state)
			return (solution_path, depth, node_count)
			
		for child in children:
			un_expanded.insert(0, child)
		un_expanded = sorted(un_expanded, key = lambda x: x.f)
