# Advent of Code 2019
import numpy as np
import pandas as pd
import math
import itertools
#%% Day 1
# Part 1
with open('2019/input/day1.txt', 'r') as file:
    input = file.readlines()
input = [i.replace('\n', '') for i in input]

req = [int(float(m)/3)-2 for m in input]
sum(req)
# req_floor = [math.floor((float(m)/3))-2 for m in input]
# sum(req_floor)

# Part 2
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
sum(reqs)

# Not 3361976, too low
# Not 8402061, too high
# Final: 5040085

def day1pt2(xlist):
    reqs = []
    for m in xlist:
        fuel =  int(float(m)/3)-2
        iter = [] 
        while fuel > 0:
            iter.append(fuel)
            fuel = int(float(fuel)/3)-2
        reqs.append(sum(iter))
    return sum(reqs)

day1pt2(input)

#%% Day 2
# Part 1
with open('2019/input/day2.txt', 'r') as file:
    input = file.readlines()
input = [int(i) for i in input[0].replace('\n','').split(',')]

input[1] = 12
input[2] = 2
    
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
day2pt1(test1)

test2 = [1,1,1,4,99,5,6,0,99]
day2pt1(test2)

day2pt1(input)

# Part 2
with open('2019/input/day2.txt', 'r') as file:
    input = file.readlines()
input = [int(i) for i in input[0].replace('\n','').split(',')]

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
            print("ERROR: Unknown Opcode.")
            break
    return x[0]

# Find all possible combinations of inputs within scope

poss = [list(comb) for comb in itertools.product(set(range(1,99,1)),repeat=2)]
# list(comb) = list of lists, comb = list of tuples, set(comb) = list of sets
# This version doesn't include dupes: [set(comb) for comb in itertools.combinations(test,2)]

def recurse_day2pt2(memory, set, target, choose=[]):
    choose
    output = day2pt2(memory,n,v)

    # Check
    if output == target:
        print("Found.")

    if output >= 
    return 

recurse_day2pt2(input,poss)


## https://stackoverflow.com/questions/4632322/finding-all-possible-combinations-of-numbers-to-reach-a-given-sum
def subset_sum(numbers, target, partial=[], partial_sum=0):
    if partial_sum == target:
        yield partial
    if partial_sum >= target:
        return
    for i, n in enumerate(numbers):
        remaining = numbers[i + 1:]
        yield from subset_sum(remaining, target, partial + [n], partial_sum + n)

