from flask import render_template, request, jsonify

from .SearchAlgorithms import RBFS, iterative_deepening_search, depth_limited_search, Astar
from .GameLogic import goal_test, find_blank_8p, actions_8p, take_action_8p
from .heuristics import h_manhattan_sum, h_hamming
from .branching import effective_branching_factor

import json

from app import app

def state_parse(json_state):
	formatted_state = json_state.split(' ')
	for i in range(0, len(formatted_state)): 
		formatted_state[i] = int(formatted_state[i])
	return formatted_state

def transform_to_flat(solution):
	path = []
	solution_tree = {}
	solution_tree['name'] = solution[0]
	solution_tree['parent'] = None
	path.append(solution_tree)
	i = 1
	
	while (i < len(solution)):
		child = {}
		child['name'] = solution[i]
		child['parent'] = solution[i - 1]
		path.append(child)
		i += 1
		
	return path
	
@app.route('/')
@app.route('/board')
def output():
	return render_template('board.html', title='8 Puzzle Solver')
	
@app.route('/receiver', methods=['POST'])
def receiver():
	search_params = request.get_json()
	print(search_params)
	
	custom_start = None
	random_start = None
	custom_end = None
	random_end = None
	algorithm = None
	heuristic = None
	max_depth = None
	depth_limit = None
	
	result = []
	start_state = []
	goal_state = []
	post_information = {}
	node_count = 0
	ebf = 0
	
	if search_params['searchParams']['custom-start']:
		custom_start = search_params['searchParams']['custom-start']
		
	if search_params['searchParams']['random-start']:
		random_start = search_params['searchParams']['random-start']
		
	if search_params['searchParams']['custom-end']:
		custom_end = search_params['searchParams']['custom-end']
		
	if search_params['searchParams']['random-end']:
		random_end = search_params['searchParams']['random-end']
		
	if search_params['searchParams']['algo']:
		algorithm = search_params['searchParams']['algo']
		
	if search_params['searchParams']['heuristic']:
		heuristic = search_params['searchParams']['heuristic']
		
	if search_params['searchParams']['max-depth']:
		max_depth = int(search_params['searchParams']['max-depth'])
		
	if search_params['searchParams']['depth-limit']:
		depth_limit = int(search_params['searchParams']['depth-limit'])
	

	start_state = state_parse(custom_start)
	goal_state = state_parse(custom_end)
	if algorithm == 'iterative-deepening':
		result, node_count = iterative_deepening_search(start_state, goal_state, actions_8p, take_action_8p, max_depth)
		ebf = effective_branching_factor(node_count, len(result) - 1)
		
	elif algorithm == 'depth-limited':
		result, node_count = depth_limited_search(start_state, goal_state, actions_8p, take_action_8p, depth_limit, node_count)
		ebf = effective_branching_factor(node_count, len(result) - 1)
		
	elif algorithm == 'recursive-best-first':
		if heuristic == 'manhattan':
			result, depth, node_count = RBFS(start_state, actions_8p, take_action_8p,
								lambda s: goal_test(s, goal_state),
								lambda s: h_manhattan_sum(s, goal_state))
		if heuristic == 'hamming':
			result, depth, node_count = RBFS(start_state, actions_8p, take_action_8p,
								lambda s: goal_test(s, goal_state),
								lambda s: h_hamming(s, goal_state))
		ebf = effective_branching_factor(node_count, depth)
						
	elif algorithm == 'a-star':
		if heuristic == 'manhattan':
			result, depth, node_count = Astar(start_state, goal_state, actions_8p, take_action_8p, lambda s: h_manhattan_sum(s, goal_state))
		if heuristic == 'hamming':
			result, depth, node_count = Astar(start_state, goal_state, actions_8p, take_action_8p, lambda s: h_hamming(s, goal_state))
		ebf = effective_branching_factor(node_count, depth)
	
	result = transform_to_flat(result)
	post_information["result"] = result
	post_information["ebf"] = ebf
	resp = jsonify(post_information)
	return resp
