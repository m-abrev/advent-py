# Advent of Code 2019
import numpy as np
import pandas as pd
import math
import itertools
#%% Day 1
### Part 1
with open('2019/input/day1.txt', 'r') as file:
    input = file.readlines()
input = [i.replace('\n', '') for i in input]

req = [int(float(m)/3)-2 for m in input]
sum(req) ## Soln: 3361976

### Part 2
## Verbose iterative form
reqs = []
n = 1
for m in input:
    print("Start with module: ", n)
    fuel =  int(float(m)/3)-2
    iter = [] 
    print("Initial fuel requirement: ", fuel)
    while fuel > 0:
        iter.append(fuel)
        print("Fuel still above zero, =", fuel)
        fuel = int(float(fuel)/3)-2
        print("That fuel's fuel:", fuel)
    reqs.append(sum(iter))
    print("Finishing module:", len(reqs))
    print("List of fuel requirements: ", reqs,"\n")
    n = n + 1
sum(reqs) ## Soln: 5040085

# ## More concise function(al) form
# def day1pt2(xlist):
#     reqs = []
#     for m in xlist:
#         fuel =  int(float(m)/3)-2
#         iter = [] 
#         while fuel > 0:
#             iter.append(fuel)
#             fuel = int(float(fuel)/3)-2
#         reqs.append(sum(iter))
#     return sum(reqs) 

# day1pt2(input) ## Soln: 5040085

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

# First function attempt (for loop per link: https://stackoverflow.com/questions/34517540/find-all-combinations-of-a-list-of-numbers-with-a-given-sum)
def search_day2pt2(memory, vars, target, output = 0):
    """ 
    Recursive function that tests all elements of a list of possibilities (vars) to determine 
    if they yield the desired Opcode output (target).

    memory (list): input list (Intcode) provided for use by the Opcode logic func, day2pt2
    vars (list): list of all possible inputs
    target (int): the output we are seeking
    output (int): input that changes with recursion and represents the "result" to be tested vs. target
    day2pt2 (func): used inside this func to call the day's Opcode logic
    """
    # output = day2pt2(memory,n,v)
    if output == target:
        print("Found. Noun and verb: ", str(n), ", ", str(v))
        print("Output: ",str(output))
        return 

    for i in range(len(vars)):
        n, v = vars[i]
        memory_rec = memory.copy()
        output_rec = day2pt2(memory,n,v) # Input (or "memory") kept having the [0] pos overwritten
        # memory = input.copy()
        print("OK we have noun ",str(n)," and verb ",str(v)," now.")
        print("We have memory with initial Opcode pointers: ", memory[0],",",memory[4],",",memory[8])
        print("The output is: ",str(output_rec))

        search_day2pt2(memory_rec, vars, target, output = output_rec)

# Second function attempt (no for loop)
def search_day2pt2(memory, vars, target, output = 0):
    """ 
    Recursive function that tests all elements of a list of possibilities (vars) to determine 
    if they yield the desired Opcode output (target).
    """
    # output = day2pt2(memory,n,v)
    if output == target:
        print("Found. Noun and verb: ", str(n), ", ", str(v))
        print("Output: ",str(output))
        return 

    n, v = vars.pop(0)
    memory_rec = memory.copy()
    output_rec = day2pt2(memory,n,v) # Input (or "memory") kept having the [0] pos overwritten
    print("OK we have noun ",str(n)," and verb ",str(v)," now.")
    print("We have memory with initial Opcode pointers: ", memory[0],",",memory[4],",",memory[8])
    print("The output is: ",str(output_rec))
    print("Our length of remaining vars is ",str(len(vars)),"\n")

    search_day2pt2(memory_rec, vars, target, output = output_rec)

# Make sure input is clean before running these fxns
with open('2019/input/day2.txt', 'r') as file:
    input = file.readlines()
input = [int(i) for i in input[0].replace('\n','').split(',')] # Need clean input

# Make a big list of all possible combinations (1,99), inclusive of duplicates like [1,1]
poss = [list(comb) for comb in itertools.product(set(range(1,100,1)),repeat=2)] # 9801 possible pairs

search_day2pt2(input.copy(), poss, 19690720)




day2pt2(input.copy(),1,1)
day2pt2(input.copy(),99,99)

#%%
## https://stackoverflow.com/questions/4632322/finding-all-possible-combinations-of-numbers-to-reach-a-given-sum
def subset_sum(numbers, target, partial=[], partial_sum=0):
    if partial_sum == target:
        yield partial
    if partial_sum >= target:
        return
    for i, n in enumerate(numbers):
        remaining = numbers[i + 1:]
        yield from subset_sum(remaining, target, partial + [n], partial_sum + n)


# %%
