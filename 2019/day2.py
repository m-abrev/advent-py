# Advent of Code 2019
import pathlib
import numpy as np
import pandas as pd
import itertools
#%% Day 2
### Part 1
with open('2019/input/day2.txt', 'r') as file:
    input = file.readlines()
input = [int(i) for i in input[0].replace('\n','').split(',')]

input[1] = 12 # Provided 
input[2] = 2 # Provided 
    
def day2pt1(x):
    """
    x: the input Intcode
    1: Opcode indicates add numbers read at positions provided by (i+1, i+2) and store at (i+3)
    2: Opcode indicates multiply numbers read at positions provided by (i+1, i+2) and store at (i+3)
    99: Opcode indicates stop
    Must step 4 ahead after processing an Opcode
    Error if reads an unknown Opcode != [1,2,99]
    """
    i = 0
    while x[i]!=99:
        if x[i]==1:
            x[x[i+3]] = x[x[i+1]] + x[x[i+2]]
            i = i + 4
        elif x[i]==2:
            x[x[i+3]] = x[x[i+1]] * x[x[i+2]]
            i = i + 4
        else: 
            print("ERROR: Unknown Opcode.")
            break
    return x[0]

test1 = [1,0,0,0,99]
day2pt1(test1) # Correct 

test2 = [1,1,1,4,99,5,6,0,99]
day2pt1(test2) # Correct

day2pt1(input) ## Soln: 6627023

### Part 2
def day2pt2(x,noun,verb):
    """
    x: the input Intcode, a list of integers and the initial memory state
    x[y] where y: an address 
    1: Opcode that indicates add numbers read at positions provided by (i+1, i+2) and store at (i+3)
    2: Opcode indicates multiply numbers read at positions provided by (i+1, i+2) and store at (i+3)
    99: Opcode indicates stop
    Must step 4 ahead after processing an Opcode
    Error if reads an unknown Opcode != [1,2,99]
    """
    i = 0
    x[1] = noun
    x[2] = verb
    # Defining Opcodes
    while x[i]!=99:
        if x[i]==1:
            x[x[i+3]] = x[x[i+1]] + x[x[i+2]]
            i = i + 4
        elif x[i]==2:
            x[x[i+3]] = x[x[i+1]] * x[x[i+2]]
            i = i + 4
        else: 
            print("ERROR: Unknown Opcode at i =",str(i))
            break
    return x[0]

target = 19690720
memory = input.copy()
poss = [list(comb) for comb in itertools.product(set(range(1,100,1)),repeat=2)] # 9801 possible pairs
for n, v in poss: 
    memory_rec = memory.copy()
    output_rec = day2pt2(memory_rec,n,v)
    print(n,v)
    print(memory_rec[0],memory_rec[1])
    if output_rec == target:
        print("Soln:", 100*n + v)
        break
    else:
        continue

## Soln: 4019 (where n = 40, v = 19)

## Watch some videos on sceop and recursion and pointers

# def search_day2pt2(memory, vars, target, output = 0):
#     """ 
#     Recursive function that tests all elements of a list of possibilities (vars) to determine 
#     if they yield the desired Opcode output (target).
#     """
#     n, v = vars.pop(0) # Fix?
#     memory_rec = memory.copy()
#     output_rec = day2pt2(memory,n,v) # Input (or "memory") kept having the [0] pos overwritten

#     # print("OK we have noun ",str(n)," and verb ",str(v)," now.")
#     # print("Our length of remaining vars is ",str(len(vars)),"\n")
#     # print("We have memory with initial Opcode pointers: ", memory[0],",",memory[4],",",memory[8])
#     # print("The output is: ",str(output_rec))

#     if output == target:
#         print("Found. Noun and verb: ", str(n), ", ", str(v))
#         print("Output: ",str(output))
#         return 
#     else:
#         search_day2pt2(memory_rec, vars, target, output = output_rec)
#     return 

# # Make sure input is clean before running these fxns
# with open('2019/input/day2.txt', 'r') as file:
#     input = file.readlines()
# input = [int(i) for i in input[0].replace('\n','').split(',')] # Need clean input

# # Make a big list of all possible combinations (1,99), inclusive of duplicates like [1,1]
# poss = [list(comb) for comb in itertools.product(set(range(1,100,1)),repeat=2)] # 9801 possible pairs

# search_day2pt2(input.copy(), poss, 19690720)

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

taxi = []
for i in range(len(xp)):
    taxi.append(abs(xp[i][0]) + abs(xp[i][1]))
    print(len(taxi))
ix = taxi.index(min(taxi))
min(taxi)

# Wrong: 2548
# Wrong: 30




x, y = list(unq.shape)


for i, j in range(x), range(y):
    print(i)


# From here we hopefully check paths for dupes then calculate the distance for each dupe 
print(start) # Confirm this is the same 

    # for i in instruction:
    #     print(i)
    #     print(start)
    #     r = snake(i,start)
    
    #     start = route[-1]
    #     np.append(route,r)
    # print("Route for Wire ", str(l),":",route)
    # np.append(paths,route)

##TODO: Troubleshoot, something wrong with how the arrays are being filled in (vstack in particular, in snake)

#%% Day 4
## Part 1


