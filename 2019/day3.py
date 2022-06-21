# Advent of Code 2019
import numpy as np
import pandas as pd
from helper import *
#%% Day 3
### Part 1
##TODO: Try this with np.meshgrid and with normal 2D arrays (not mgrid, ints dont have steps issue)

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

test_i = 'U15'
test_s = np.array([0,0])
test_r1 = snake(test_i,test_s)
test_i = 'R3'
test_s = test_r1[-1]
test_r2 = snake(test_i,test_s)
test_r3 = np.vstack((test_r1,test_r2))
test_r3

with open('2019/input/day3.txt', 'r') as file:
    input = file.read().splitlines()

# paths = np.empty((2,2)) # Both routes will be appended to this after the fact, and then checked for dupes
# for l in range(len(input)): # 2 entries
#     start = np.array([0,0])
#     instruction = input[l].split(',')
#     route = np.empty((2,2)) # for each line you need a route
#     for i in range(len(instruction)):
#         r = snake(instruction[i],start) # Start must be dynamic
#         route = np.vstack((route,r)) # Adds new route to prev path 
#         start = route[-1] # Reset starting point for next instruction input
#     routes = np.unique(route, axis=0,) # Attempt to cut out duplicates
#     paths = np.vstack((paths,routes)).astype(int)

patha = np.empty((2,2))

start = np.array([0,0])
instruction = input[0].split(',')
route = np.empty((2, 2))  # for each line you need a route
for i in range(len(instruction)):
    r = snake(instruction[i], start)  # Start must be dynamic
    route = np.vstack((route, r))  # Adds new route to prev path
    start = route[-1]  # Reset starting point for next instruction input
routes = np.unique(route, axis=0,)  # Attempt to cut out duplicates
patha = np.vstack((patha, routes)).astype(int)

pathb = np.empty((2,2))
start = np.array([0,0])
instruction = input[1].split(',')
route = np.empty((2, 2))  # for each line you need a route
for i in range(len(instruction)):
    r = snake(instruction[i], start)  # Start must be dynamic
    route = np.vstack((route, r))  # Adds new route to prev path
    start = route[-1]  # Reset starting point for next instruction input
routes = np.unique(route, axis=0,)  # Attempt to cut out duplicates
pathb = np.vstack((pathb, routes)).astype(int)

unq, count = np.unique(paths, axis=0, return_counts=True)
xp = unq[count>1] # This is a bad sign, multiple dupes
print("Number of total steps", paths.shape[0], " of which ", paths.shape[0]-unq.shape[0], " are Xs.")

xp.shape

plt.scatter(patha[:,0], patha[:,1], marker=".", c="orange", s=1)
plt.scatter(pathb[:,0], pathb[:,1], marker=".", c="salmon", s=1)
plt.scatter(xp[:,0], xp[:,1], marker="o", c="dodgerblue", s=3)
plt.scatter(0, 0, marker="*", c="navy", s=4)
plt.show()

plt.clf()

plt.cla()

taxi = []
for i in range(len(xp)):
    taxi.append(abs(xp[i][0]) + abs(xp[i][1]))
    print(len(taxi))
ix = taxi.index(min(taxi))
min(taxi)

# Wrong: 2548
# Wrong: 30



