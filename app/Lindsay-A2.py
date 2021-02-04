#!/usr/bin/env python
# coding: utf-8

# 
# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Assignment-2:-Iterative-Deepening-Search" data-toc-modified-id="Assignment-2:-Iterative-Deepening-Search-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Assignment 2: Iterative-Deepening Search</a></span><ul class="toc-item"><li><span><a href="#Overview" data-toc-modified-id="Overview-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Overview</a></span></li><li><span><a href="#Required-Code" data-toc-modified-id="Required-Code-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Required Code</a></span></li><li><span><a href="#Grading-and-Check-in" data-toc-modified-id="Grading-and-Check-in-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Grading and Check in</a></span></li><li><span><a href="#Extra-Credit" data-toc-modified-id="Extra-Credit-1.4"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Extra Credit</a></span></li></ul></li></ul></div>

# # Assignment 2: Iterative-Deepening Search

# ### By Josh Lindsay

# ## Overview

# Implement  the iterative-deepening search algorithm as discussed in our lecture notes and as shown in figures 3.17 and 3.18 in our text book. Apply it to the 8-puzzle and a second puzzle of your choice. 

# ## Required Code

# In this jupyter notebook, implement the following functions:
# 
#   * `iterative_deepening_search(start_state, goal_state, actions_f, take_action_f, max_depth)`
#   * `depth_limited_search(start_state, goal_state, actions_f, take_action_f, depth_limit)`
#   
# `depth_limited_search` is called by `iterative_deepening_search` with `depth_limit`s of $0, 1, \ldots, $ `max_depth`. Both must return either the solution path as a list of states, or the strings `'cutoff'` or `'failure'`.  `'failure'` signifies that all states were searched and the goal was not found. 
# 
# Each receives the arguments
# 
#   * the starting state, 
#   * the goal state,
#   * a function `actions_f` that is given a state and returns a list of valid actions from that state,
#   * a function `take_action_f` that is given a state and an action and returns the new state that results from applying the action to the state,
#   * either a `depth_limit` for `depth_limited_search`, or `max_depth` for `iterative_deepening_search`.

# Use your solution to solve the 8-puzzle.
# Implement the state of the puzzle as a list of integers. 0 represents the empty position. 
# 
# Required functions for the 8-puzzle are the following.
# 
#   * `find_blank_8p(state)`: return the row and column index for the location of the blank (the 0 value).
#   * `actions_f_8p(state)`: returns a list of up to four valid actions that can be applied in `state`. Return them in the order `left`, `right`, `up`, `down`, though only if each one is a valid action.
#   * `take_action_f_8p(state, action)`: return the state that results from applying `action` in `state`.
#   * `print_state_8p(state)`: prints the state as a 3 x 3 table, as shown in lecture notes, or a bit fancier with, for example, '-' and '|' characters to separate tiles.  This function is useful to call when debugging your search algorithms.
#   * `print_path_8p(start_state, goal_state, path)`: print a solution path in a readable form by calling `print_state_8p`.

# <font color='red'>Also, implement a second search problem of your choice.  Apply your `iterative_deepening_search` function to it.</font>

# In[1]:


def depth_limited_search(start_state, goal_state, actions_f, take_action_f, depth_limit):
    if start_state == goal_state:
        return []
    if depth_limit == 0:
        return 'cutoff'
    
    cutoff_occurred = False
    for action in actions_f(start_state):
        child_state = take_action_f(start_state, action)
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


# In[2]:


def iterative_deepening_search(start_state, goal_state, actions_f, take_action_f, max_depth):
    for depth in range(max_depth):
        result = depth_limited_search(start_state, goal_state, actions_f, take_action_f, depth)
        
        if result is 'failure':
            return 'failure'
        if result is not 'cutoff':
            result.insert(0, start_state)
            return result
    return 'cutoff'


# In[3]:


def find_blank_8p(start_state):
    ss_copy = list(start_state)
    blank = ss_copy.index(0)
    return (blank // 3, blank % 3)


# In[4]:


def actions_f_8p(start_state):
    actions = []
    blank = find_blank_8p(start_state)
    
    if blank[1] != 0:
        actions.append('left')
    if blank[1] != 2:
        actions.append('right')
    if blank[0] != 0:
        actions.append('up')
    if blank[0] != 2:
        actions.append('down')
    return actions


# In[5]:


def take_action_f_8p(start_state, action):
    ss_copy = list(start_state)
    blank = ss_copy.index(0)
    actions = actions_f_8p(ss_copy)
    
    if action == 'left' and action in actions:
        ss_copy[blank], ss_copy[blank - 1] = ss_copy[blank - 1], ss_copy[blank]
    if action == 'right' and action in actions:
        ss_copy[blank], ss_copy[blank + 1] = ss_copy[blank + 1], ss_copy[blank]
    if action == 'up' and action in actions:
        ss_copy[blank], ss_copy[blank - 3] = ss_copy[blank - 3], ss_copy[blank]
    if action == 'down' and action in actions:
        ss_copy[blank], ss_copy[blank + 3] = ss_copy[blank + 3], ss_copy[blank]
    return ss_copy


# In[6]:


def print_state_8p(start_state, padding=0):
    blank = start_state.index(0)
    ss_copy = list(start_state)
    ss_copy[blank] = '-'
    print(' '*padding + f'{ss_copy[0]} {ss_copy[1]} {ss_copy[2]}')
    print(' '*padding + f'{ss_copy[3]} {ss_copy[4]} {ss_copy[5]}')
    print(' '*padding + f'{ss_copy[6]} {ss_copy[7]} {ss_copy[8]}')


# In[7]:


def print_path_8p(start_state, goal_state, path):
    print('Path from')
    print_state_8p(start_state)
    print(' to')
    print_state_8p(goal_state)
    print(f' is {len(path)} nodes long')
    
    for pad in range(len(path)):
        print_state_8p(path[pad], pad)
        print()


# Here are some example results.

# In[8]:


start_state = [1, 0, 3, 4, 2, 5, 6, 7, 8]


# In[13]:


print_state_8p(start_state)


# In[14]:


find_blank_8p(start_state)


# In[15]:


actions_f_8p(start_state)


# In[18]:


take_action_f_8p(start_state, 'down')


# In[19]:


print_state_8p(take_action_f_8p(start_state, 'down'))


# In[20]:


goal_state = take_action_f_8p(start_state, 'down')


# In[21]:


new_state = take_action_f_8p(start_state, 'down')


# In[22]:


new_state == goal_state


# In[23]:


start_state


# In[24]:


path = depth_limited_search(start_state, goal_state, actions_f_8p, take_action_f_8p, 3)
path


# Notice that `depth_limited_search` result is missing the start state.  This is inserted by `iterative_deepening_search`.
# 
# But, when we try `iterative_deepening_search` to do the same search, it finds a shorter path!

# In[26]:


path = iterative_deepening_search(start_state, goal_state, actions_f_8p, take_action_f_8p, 3)
path


# Also notice that the successor states are lists, not tuples.  This is okay, because the search functions for this assignment do not make use of python dictionaries.

# In[20]:


start_state = [4, 7, 2, 1, 6, 5, 0, 3, 8]
path = iterative_deepening_search(start_state, goal_state, actions_f_8p, take_action_f_8p, 3)
path


# In[27]:


start_state = [4, 7, 2, 1, 6, 5, 0, 3, 8]
path = iterative_deepening_search(start_state, goal_state, actions_f_8p, take_action_f_8p, 5)
path


# Humm...maybe we can't reach the goal state from this state.  We need a way to randomly generate a valid start state.

# In[28]:


import random


# In[29]:


random.choice(['left', 'right', 'down', 'up'])


# In[30]:


def random_start_state(goal_state, actions_f, take_action_f, n_steps):
    state = goal_state
    for i in range(n_steps):
        state = take_action_f(state, random.choice(actions_f(state)))
    return state


# In[31]:


goal_state = [1, 2, 3, 4, 0, 5, 6, 7, 8]
random_start_state(goal_state, actions_f_8p, take_action_f_8p, 10)


# In[32]:


start_state = random_start_state(goal_state, actions_f_8p, take_action_f_8p, 30)
start_state


# In[33]:


path = iterative_deepening_search(start_state, goal_state, actions_f_8p, take_action_f_8p, 20)
path


# Let's print out the state sequence in a readable form.

# In[34]:


for p in path:
    print_state_8p(p)
    print()


# Here is one way to format the search problem and solution in a readable form.

# In[35]:


print_path_8p(start_state, goal_state, path)


# ## Discussion

# For solving 8-puzzles, the iterative-deepening search method seems to work well on puzzles with a low number of random steps chosen. Once the number of steps is >200, the algorithm slows down significantly, at least on my hardware. Occasionally for small amounts of random steps, I find that IDS doesn't find the solution in the minimum number of steps. Particularly for boards with 50 random steps, I find solutions that can be solved in 1-2 fewer steps. This makes sense since IDS is uninformed, so it's not always going to find the optimal path, but it's interesting nonetheless.

# # Iterative-Deepening Search on a 15-Puzzle

# For the puzzle of my choice, I'm running iterative-deepening search on a 15-puzzle.

# In[30]:


def find_blank_15p(start_state):
    ss_copy = list(start_state)
    blank = ss_copy.index(0)
    return (blank // 4, blank % 4)


# In[31]:


def actions_f_15p(start_state):
    actions = []
    blank = find_blank_15p(start_state)
    
    if blank[1] != 0:
        actions.append('left')
    if blank[1] != 3:
        actions.append('right')
    if blank[0] != 0:
        actions.append('up')
    if blank[0] != 3:
        actions.append('down')
    return actions


# In[32]:


def take_action_f_15p(start_state, action):
    ss_copy = list(start_state)
    blank = ss_copy.index(0)
    actions = actions_f_15p(ss_copy)
    
    if action == 'left' and action in actions:
        ss_copy[blank], ss_copy[blank - 1] = ss_copy[blank - 1], ss_copy[blank]
    if action == 'right' and action in actions:
        ss_copy[blank], ss_copy[blank + 1] = ss_copy[blank + 1], ss_copy[blank]
    if action == 'up' and action in actions:
        ss_copy[blank], ss_copy[blank - 4] = ss_copy[blank - 4], ss_copy[blank]
    if action == 'down' and action in actions:
        ss_copy[blank], ss_copy[blank + 4] = ss_copy[blank + 4], ss_copy[blank]
    return ss_copy


# In[33]:


def print_state_15p(start_state, padding=0):
    blank = start_state.index(0)
    ss_copy = list(start_state)
    ss_copy[blank] = '--'
    
    print(' '*padding + f'{str(ss_copy[0]).zfill(2)} {str(ss_copy[1]).zfill(2)} {str(ss_copy[2]).zfill(2)} {str(ss_copy[3]).zfill(2)}')
    print(' '*padding + f'{str(ss_copy[4]).zfill(2)} {str(ss_copy[5]).zfill(2)} {str(ss_copy[6]).zfill(2)} {str(ss_copy[7]).zfill(2)}')
    print(' '*padding + f'{str(ss_copy[8]).zfill(2)} {str(ss_copy[9]).zfill(2)} {str(ss_copy[10]).zfill(2)} {str(ss_copy[11]).zfill(2)}')
    print(' '*padding + f'{str(ss_copy[12]).zfill(2)} {str(ss_copy[13]).zfill(2)} {str(ss_copy[14]).zfill(2)} {str(ss_copy[15]).zfill(2)}')


# In[34]:


def print_path_15p(start_state, goal_state, path):
    print('Path from')
    print_state_15p(start_state)
    print(' to')
    print_state_15p(goal_state)
    print(f' is {len(path)} nodes long')
    print()
    for pad in range(len(path)):
        print_state_15p(path[pad], pad)
        print()


# In[35]:


goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
start_state = random_start_state(goal_state, actions_f_15p, take_action_f_15p, 30)
start_state


# In[36]:


path = iterative_deepening_search(start_state, goal_state, actions_f_15p, take_action_f_15p, 20)
path


# In[37]:


print_path_15p(start_state, goal_state, path)


# ## Discussion

# The second search problem I chose was a 15-puzzle, a version of the 8 puzzle but with 15 blocks on a 4x4 grid instead of 7 blocks on a 3x3 grid. The way I implemented it is essentially the same as the 8-puzzle but with more outputs and different indexing values for finding blanks and checking/executing actions. For the 8-puzzle, I would work with offsets of 3 for indexing because it's a 3x3 puzzle, so for the 15-puzzle, I used offsets of 4 since it's a 4x4 puzzle. In terms of solutions, I found that the 15-puzzle took much longer to generate solutions than 8-puzzles across all values. Not only were there more nodes in the solution path on average, but determining the next node to jump to took longer, maybe because the nodes are larger. The main question I would ask is whether the placement of the empty sapce has an impact on performace. In my tests, I put it at the coordinate (3, 3), but maybe if it was somewhere else, especially in the middle 4 points, the solving speed would be faster. 

# ## Grading and Check in

# Download [A2grader.tar](A2grader.tar) and extract A2grader.py from it, before running next code cell.

# In[38]:


get_ipython().run_line_magic('run', '-i A2grader.py')


# Check in your notebook for Assignment 2 on our [Canvas site](https://colostate.instructure.com/courses/109411).
