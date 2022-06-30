# Advent of Code 2019
import numpy as np
import pandas as pd
from helper import *
import matplotlib.pyplot as plt
#%% Day 3
## Part 1
##TODO: Try this with different methods (np.meshgrid?) 

def snake(inst, start): # TODO: Handle intake of a list and not of a specific instruction
    """
    inst: list (or 2x1 np array) of instructions
    start: 2x1 np array providing the starting point of a path (x,y)
    """
    x1, y1 = start[0], start[1]
    steps = int(inst[1:]) + 1 # Account for 0 indexing

    if inst[0]=="U":
        x = x1*np.ones(steps) # Does not change
        y = np.arange(y1, y1+steps) # Increases from start to final, accounting for start
    elif inst[0]=="D":
        x = x1*np.ones(steps)
        y = np.arange(y1, y1-steps, -1) # Needs negative argument
    elif inst[0]=="R":
        x = np.arange(x1, x1+steps)
        y = y1*np.ones(steps)
    elif inst[0]=="L":
        x = np.arange(x1, x1-steps, -1) # Needs negative argument
        y = y1*np.ones(steps)
    else: # raise exception
        print("ERROR")
        return
    return np.vstack((x,y)).transpose() # 2D array knitting together our two row vectors into (x,y) "columns"

# Confirm snake works
test_r1 = snake('U15', np.array([0,0]))
test_r2 = snake('R3', test_r1[-1])
print("Test snake: ", np.vstack((test_r1,test_r2)))

# Begin
with open('2019/input/day3.txt', 'r') as file:
    input = file.read().splitlines()

paths_list = [] # Create path for each set of instructions (entry in paths_list)
for l in range(len(input)): 
    start = np.array([0,0]) # Central starting point 
    instruction = input[l].split(',')
    route = np.zeros((2),int) # For each instruction you need an empty array init'd
    for i in range(len(instruction)):
        r = snake(instruction[i],start) # Route followed given [i]th instruction in input
        route = np.vstack((route,r)).astype(int) # Adds new route to prev route  
        start = route[-1] # Reset strarting point for next instruction input
    paths_list.append(route[1:]) # Need to strip the very first row out before appending (np quirk)

# Part 1. Find intersections and report on the "closest" intersection (to the origin)
paths = np.vstack((np.unique(paths_list[0], axis=0),
        np.unique(paths_list[1],axis=0))).astype(int) # Make one large list of steps in both paths (unordered)
unq, count = np.unique(paths, axis=0, return_counts=True)
xp = unq[count>1] # len(xp) = 39 intersections
xp = xp[np.where((xp!=(0,0)).all(axis=1))]
print("Number of total steps", paths.shape[0], " of which ", paths.shape[0]-unq.shape[0], " are Xs.")

# Use Manhattan distance on each xpt and find minimum
taxi = []
for i in range(len(xp)):
    taxi.append(abs(xp[i][0]) + abs(xp[i][1]))
taxi.remove(0)
min(taxi)

# Soln: 557

#%% Day 3
## Part 2
p0 = paths_list[0]
p1 = paths_list[1]
c = []
for x in xp: # Awk because I should have deleted [0,0]
    a = np.where((p0==x).all(axis=1)) # Steps to reach that intersection
    b = np.where((p1==x).all(axis=1)) # Steps to reach that intersection
    c.append(a[0][0] + b[0][0])
min(c)


# Same but different
paths_list = [] # Create path for each set of instructions (entry in paths_list)
for l in range(len(input)): 
    start = np.array([0,0]) # Central starting point 
    instruction = input[l].split(',')
    route = np.zeros((2),int) # For each instruction you need an empty array init'd
    for i in range(len(instruction)):
        r = snake(instruction[i],start) # Route followed given [i]th instruction in input
        route = np.vstack((route,r)).astype(int) # Adds new route to prev route  
        start = route[-1] # Reset strarting point for next instruction input
    paths_list.append(route[1:]) # Need to strip the very first row out before appending (np quirk)

# P






# Fuck this


for i in range(min(len(patha),len(pathb))):
    # if np.array_equiv(patha[i],pathb[i]):
    #     print("Found an intersection:", i)
    #     continue
    if (patha[i] in xp[xp!=[0,0]]):
        print("Found a patha intersection at ", i, " and ", patha[i])
    if  (pathb[i] in xp[xp!=[0,0]]):
        print("Found a pathb intersection at ", i, " and ", pathb[i])
    else:
        continue

unq, idx, count = np.unique(paths, axis=0, return_index=True, return_counts=True)
min(idx[count>1]) 

# Wrong: 2230 (too low?), 56523, 56521 (too high?)

## Graveyard
# patha = np.empty((2,2))

# start = np.array([0,0])
# instruction = input[0].split(',')
# route = np.empty((2, 2))  # for each line you need a route
# for i in range(len(instruction)):
#     r = snake(instruction[i], start)  # Start must be dynamic
#     route = np.vstack((route, r))  # Adds new route to prev path
#     start = route[-1]  # Reset starting point for next instruction input
# routes = np.unique(route, axis=0,)  # Attempt to cut out duplicates
# patha = np.vstack((patha, routes)).astype(int)

# pathb = np.empty((2,2))
# start = np.array([0,0])
# instruction = input[1].split(',')
# route = np.empty((2, 2))  # for each line you need a route
# for i in range(len(instruction)):
#     r = snake(instruction[i], start)  # Start must be dynamic
#     route = np.vstack((route, r))  # Adds new route to prev path
#     start = route[-1]  # Reset starting point for next instruction input
# routes = np.unique(route, axis=0,)  # Attempt to cut out duplicates
# pathb = np.vstack((pathb, routes)).astype(int)

# plt.cla()
# plt.scatter(patha[:,0], patha[:,1], marker=".", c="orange", s=1)
# plt.scatter(pathb[:,0], pathb[:,1], marker=".", c="salmon", s=1)
# plt.scatter(xp[:,0], xp[:,1], marker="o", c="dodgerblue", s=3)
# plt.scatter(0, 0, marker="*", c="navy", s=4)
# plt.show()

