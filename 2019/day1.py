# Advent of Code 2019
import pathlib
import numpy as np
import pandas as pd
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
