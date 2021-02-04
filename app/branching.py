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
