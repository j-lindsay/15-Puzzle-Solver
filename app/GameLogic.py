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
