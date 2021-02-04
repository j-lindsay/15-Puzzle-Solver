import pandas
import sys
from IPython.display import display_html 

class Node:

    def __init__(self, state, f=0, g=0, h=0):
        self.state = state
        self.f = f
        self.g = g
        self.h = h
    def __repr__(self):
        return f'Node({self.state}, f={self.f}, g={self.g}, h={self.h})'

def Astar_search(start_state, actions_f, take_action_f, goal_test_f, h_f):
    global node_count
    node_count = 0
    h = h_f(start_state)
    g = 0
    start_node = Node(state=start_state, f=(g + h), g=g, h=h)
    return Astar_search_helper(start_node, actions_f, take_action_f, goal_test_f, h_f, float('inf'))

def Astar_search_helper(parent_node, actions_f, take_action_f, goal_test_f, h_f, f_max):
    global node_count
    if goal_test_f(parent_node.state):
        return ([parent_node.state], parent_node.g)
    
    actions = actions_f(parent_node.state)
    if not actions:
        return ('failure', float('inf'))
    
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
            return ('failure', best_child.f)
        alternative_f = children[1].f if len(children) > 1 else float('inf')
        result, best_child.f = Astar_search_helper(best_child, actions_f, take_action_f, 
                                                    goal_test_f, h_f, min(f_max,alternative_f))
        if result != 'failure':                  
            result.insert(0, parent_node.state)    
            return (result, best_child.f)  

def iterative_deepening_search(start_state, goal_state, actions_f, take_action_f, max_depth):
    global node_count
    for depth in range(max_depth):
        node_count = 0
        result = depth_limited_search(start_state, goal_state, actions_f, take_action_f, depth)
        
        if result is 'failure':
            return 'failure'
        if result is not 'cutoff':
            result.insert(0, start_state)
            return result
    return 'cutoff'

def depth_limited_search(start_state, goal_state, actions_f, take_action_f, depth_limit):
    global node_count
    if start_state == goal_state:
        return []
    if depth_limit == 0:
        return 'cutoff'
    
    cutoff_occurred = False
    for action in actions_f(start_state):
        node_count += 1
        
        child_state, step_cost = take_action_f(start_state, action)
        result = depth_limited_search(child_state, goal_state, actions_f, take_action_f, depth_limit - 1)
        
        if result is 'cutoff':
            cutoff_occurred = True
        elif result is not 'failure':
            result.insert(0, child_state)
            return result
    
    if cutoff_occurred:
        return 'cutoff'
    else:
        return 'failure'

def guess(b, d):
    if b != 1:
        num = 1 - b**(d + 1)
        denom = 1 - b
        return num / denom
    else:
        return d + 1
    
def effective_branching_factor(n_nodes, depth, precision=0.01):
    error = n_nodes * precision
    low = 0
    high = n_nodes
    mid = 0
    node_guess = 0
    
    while (abs(node_guess - n_nodes) > error):
        mid = (high + low)/2
        node_guess = guess(mid, depth)
        if node_guess < n_nodes:
            low = mid
        elif node_guess > n_nodes:
            high = mid
            
    p = str(precision)
    length = len(p) - 2
    return round(mid, length)

def goal_test(state, goal):
    return state == goal

def find_blank_8p(start_state):
    ss_copy = list(start_state)
    blank = ss_copy.index(0)
    return (blank // 3, blank % 3)

def actions_8p(start_state):
    actions = []
    blank = find_blank_8p(start_state)
    
    if blank[1] != 0:
        actions.append(('left', 1))
    if blank[1] != 2:
        actions.append(('right', 1))
    if blank[0] != 0:
        actions.append(('up', 1))
    if blank[0] != 2:
        actions.append(('down', 1))
    return actions

def take_action_8p(start_state, action):
    ss_copy = list(start_state)
    blank = ss_copy.index(0)
    actions = actions_8p(ss_copy)
    
    if action[0] == 'left' and action in actions:
        ss_copy[blank], ss_copy[blank - 1] = ss_copy[blank - 1], ss_copy[blank]
    if action[0] == 'right' and action in actions:
        ss_copy[blank], ss_copy[blank + 1] = ss_copy[blank + 1], ss_copy[blank]
    if action[0] == 'up' and action in actions:
        ss_copy[blank], ss_copy[blank - 3] = ss_copy[blank - 3], ss_copy[blank]
    if action[0] == 'down' and action in actions:
        ss_copy[blank], ss_copy[blank + 3] = ss_copy[blank + 3], ss_copy[blank]
    return (ss_copy, action[1])

def print_state_8p(start_state, padding=0):
    blank = start_state.index(0)
    ss_copy = list(start_state)
    ss_copy[blank] = '-'
    print(' '*padding + f'{ss_copy[0]} {ss_copy[1]} {ss_copy[2]}')
    print(' '*padding + f'{ss_copy[3]} {ss_copy[4]} {ss_copy[5]}')
    print(' '*padding + f'{ss_copy[6]} {ss_copy[7]} {ss_copy[8]}')
    
def print_path_8p(start_state, goal_state, path):
    print('Path from')
    print_state_8p(start_state)
    print(' to')
    print_state_8p(goal_state)
    print(f' is {len(path)} nodes long')
    
    for pad in range(len(path)):
        print_state_8p(path[pad], pad)
        print()
        
def find_blank_15p(start_state):
    ss_copy = list(start_state)
    blank = ss_copy.index(0)
    return (blank // 4, blank % 4)

def actions_f_15p(start_state):
    actions = []
    blank = find_blank_15p(start_state)
    
    if blank[1] != 0:
        actions.append(('left', 1))
    if blank[1] != 3:
        actions.append(('right', 1))
    if blank[0] != 0:
        actions.append(('up', 1))
    if blank[0] != 3:
        actions.append(('down', 1))
    return actions

def take_action_f_15p(start_state, action):
    ss_copy = list(start_state)
    blank = ss_copy.index(0)
    actions = actions_f_15p(ss_copy)
    
    if action[0] == 'left' and action in actions:
        ss_copy[blank], ss_copy[blank - 1] = ss_copy[blank - 1], ss_copy[blank]
    if action[0] == 'right' and action in actions:
        ss_copy[blank], ss_copy[blank + 1] = ss_copy[blank + 1], ss_copy[blank]
    if action[0] == 'up' and action in actions:
        ss_copy[blank], ss_copy[blank - 4] = ss_copy[blank - 4], ss_copy[blank]
    if action[0] == 'down' and action in actions:
        ss_copy[blank], ss_copy[blank + 4] = ss_copy[blank + 4], ss_copy[blank]
    return (ss_copy, action[1])

def h1_8p(state, goal):
    return 0

def h2_8p(state, goal):
    x1, y1 = find_blank_8p(state)
    x2, y2 = find_blank_8p(goal)
    m = abs(x1 - x2) + abs(y1 - y2)
    return m

def h3_8p(state, goal):
    x1, y1 = find_blank_8p(state)
    x2, y2 = find_blank_8p(goal)
    d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    return d
    
def h2_15p(state, goal):
    x1, y1 = find_blank_15p(state)
    x2, y2 = find_blank_15p(goal)
    m = abs(x1 - x2) + abs(y1 - y2)
    return m

def run_experiment(goal_state_1, goal_state_2, goal_state_3, h_list):
    global node_count
    start_state = [1,  2,  3,  4,  0,  5,  6,  7,  8]
    goal_states = [goal_state_1, goal_state_2, goal_state_3]
    max_depth = sys.maxsize
    result_list = []
    
    for goal_state in goal_states:
        h_index = 1
        node_count = 0
        result = iterative_deepening_search(start_state, goal_state, actions_8p, take_action_8p, max_depth)
        result_list.append(("IDS", len(result)-1, node_count, 
                                                effective_branching_factor(node_count, len(result) - 1)))
        for h in h_list:
            node_count = 0
            (result, depth) = Astar_search(start_state, actions_8p, take_action_8p,
                        lambda s: goal_test_8p(s, goal_state),
                        lambda s: h(s, goal_state))
            result_list.append(("A*h" + str(h_index), depth, node_count, effective_branching_factor(node_count, depth)))
            h_index += 1
    return result_list
# print(run_experiment([1, 2, 3, 4, 0, 5, 6, 7, 8],[1, 2, 3, 4, 5, 8, 6, 0, 7],[1, 0, 3, 4, 5, 8, 2, 6, 7],[h1_8p, h2_8p, h3_8p]))

start_state = [1, 2, 3, 4, 5, 0, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
goal_state = [1, 2, 3, 4, 0, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
path, depth = Astar_search(start_state, actions_f_15p, take_action_f_15p,
                        lambda s: goal_test(s, goal_state),
                        lambda s: h2_15p(s, goal_state))
print(path)

effective_branching_factor(10, 3)
effective_branching_factor(1, 0)
effective_branching_factor(2, 1)
effective_branching_factor(2, 1, precision=0.000001)
effective_branching_factor(200000, 5)
effective_branching_factor(200000, 50)


'''
exp_results1 = pandas.DataFrame(result_list[0:4], columns=['Algorithm', 'Depth', 'Nodes', 'EBF'])
exp_results2 = pandas.DataFrame(result_list[4:8], columns=['Algorithm', 'Depth', 'Nodes', 'EBF'])
exp_results3 = pandas.DataFrame(result_list[8:12], columns=['Algorithm', 'Depth', 'Nodes', 'EBF'])

exp1_styler = exp_results1.style.set_table_attributes("style='display:inline'").set_caption(goal_state_1)
exp2_styler = exp_results2.style.set_table_attributes("style='display:inline'").set_caption(goal_state_2)
exp3_styler = exp_results3.style.set_table_attributes("style='display:inline'").set_caption(goal_state_3)

display_html(exp1_styler._repr_html_() + (10*"\xa0") + exp2_styler._repr_html_() + (10*"\xa0") + exp3_styler._repr_html_(), raw=True)
'''
