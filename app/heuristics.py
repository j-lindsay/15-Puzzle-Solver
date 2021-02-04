def h_manhattan_sum(state, goal):
    total = 0
    row = 0
    col = 0
    
    for element in state:
        goal_position = goal.index(element)
        
        goal_row = goal_position // 3
        goal_col = goal_position % 3
        
        total += abs(row - goal_row) + abs(col - goal_col)
        
        if (col != 2):
            col += 1
        else:
            row +=1
            col = 0
            
    return (total // 2)
    
def h_hamming(state, goal):
    wrongPosition = 0
    for s,g in zip(state, goal):
        if s != g:
            wrongPosition += 1
    return wrongPosition
