# -*- coding: utf-8 -*-
"""
@author: Maddie

Start Date : Sun Dec 20 07:55:32 2020

C:\Python37\Projects\ADVENT_2020

Title :  Advent of Code 2020

Goal : Give this a shot. (1. Attempt, 2. Learn, 3. Critique and Improve)

Outcomes : Complete each puzzle pair for 25 days of AOC.

"""
#%% DAY 1
# Setup
import time
import pandas as pd
import numpy as np
t0 = time.time()

# Input
expense_report = open("C:\Python37\Projects\ADVENT_2020\input\day1.txt",'r').read().split()
expenses = [int(i) for i in expense_report]
del expense_report

# Puzzle 1---------------------------------------------------------------------
# Task: Search for two numbers in expense report that add to equal 2020.
# Fill array with report elems where report vals are added row and colwise.
sheet = np.zeros([200,200]) # Use symmetric matrix feat instead?
for i in range(len(expenses)):
    sheet[i] = [expenses[j]+expenses[i] for j in range(len(expenses))]
# Search np array to find 2020. Return position in array. Used: loc = np.where(sheet == 2020)[0].tolist()
s1 = expenses[np.where(sheet == 2020)[0].tolist()[0]]*expenses[np.where(sheet == 2020)[0].tolist()[1]]
# Correct.
t1 = time.time()

# Puzzle 2---------------------------------------------------------------------
# Task: Same but with three numbers within expenses, instead of two.
# Attempt using old sheet and adding, searching similarly. 
sheet_0 = np.zeros([200,200]) 
for i in range(len(expenses)):
    sheet_0 =  sheet+expenses[i]
    loc = np.where(sheet_0 == 2020)
    if np.any(loc):
        solution_loc = loc[0]
        solu = sheet_0[loc[0][0],loc[0][1]] # Not sure why but this returns 2020?
        val1 = expenses[loc[0][0]]
        val2 = expenses[loc[0][1]]
        val3 = expenses[i]
s2 = val1 * val2 * val3
# Correct. 
t2 = time.time()
d1_t = t2-t0 # Log 

'''
Day 1 Drawing Board
# Attempt: convert all values in original array that were less than 2020 into a 1D array
# Add each individual expense values to that 1D (to create a 2D).
# Search that 2D.

# Try using while loop to streamline: stop when one 2020
while i <> 2020:
    # ... stuff ...
    filter_arr = sheet_line == 2020 # Can you do == here?
    new_line = sheet_line[filter_arr]
        
# The matrix is symmetric: could search only 1/2 to save time? 
il1 = np.tril_indices(200) # Use to index all below diag of matrix
array[il1] # Returns vals in lower triang

# After the fact: thinking "zip" may be something to try. Allows for multiple 
# dims in a loop, i.e.:
for a,b in zip(xrange(10), xrange(10)):
    a+b
And you get a list of length 10 where each is the first item + second item.
'''
#%% DAY 2
# Setup
import time
import pandas as pd
import re 
t0 = time.time()

# Input
password_list = open("C:\Python37\Projects\ADVENT_2020\input\day2.txt",'r').read().replace(" ","").splitlines()
password_dict = [password_list[i].split(':') for i in range(len(password_list))]
password_dict = [re.split(':|-',password_list[i]) for i in range(len(password_list))]
# Probably use re instead because split only accepts one delim
# Puzzle 1---------------------------------------------------------------------
# Task: Confirm each password has between a and b of the designated char in it.
# Splice each entry here: first entry = 'a-bX', second entry = '______' nonstandard random string to be counted
ct = 0
for i in range(len(password_dict)): 
    a = int(password_dict[i][0]) # ID lower bound of cha necessary
    b = int(password_dict[i][1][0:-1]) # ID upper bound of cha necessary
    cha = password_dict[i][1][-1] # ID character necessary
    pwd = password_dict[i][2] # ID password to check for chars
    if a <= pwd.count(cha) <= b:
        ct = ct + 1 
s1 = ct
# Correct.
t1 = time.time()

# Puzzle 2---------------------------------------------------------------------
# Task: Confirm that for the given indices (2) each pwd has only 1 char present. 
ct = 0
for i in range(len(password_dict)): 
    a = int(password_dict[i][0]) - 1 # ID first of two indices; note lack of zero indexing
    b = int(password_dict[i][1][0:-1]) - 1 # ID second of two indices; note lack of zero indexing
    cha = password_dict[i][1][-1] # ID the character of interest
    pwd_index = password_dict[i][2][a] + password_dict[i][2][b] # Sum checks of cha on selected indices
    if pwd_index.count(cha) == 1:
        ct = ct + 1

s2 = ct
# Correct.
t2 = time.time()
d2_t = t2-t0 # Log 

'''
Day 2 Drawing Board
# Long version: is it better to be explicit or jam everything in one line of 
an if statement? Who knows.

a = []
b = []
cha = []
pwd = []
ct = 0
for i in range(len(password_dict)): 
    a.append(password_dict[i][0])
    b.append(password_dict[i][1][0:-1])
    cha.append(password_dict[i][1][-1])
    pwd.append(password_dict[i][2])
    if int(password_dict[i][0]) <= password_dict[i][2].count(password_dict[i][1][-1]) <= int(password_dict[i][1][0:-1]):
        ct = ct + 1

'''
#%% DAY 3
# Setup 
import time
import pandas as pd
import numpy as np 
t0 = time.time()

# Input 
inp0 = open("C:\Python37\Projects\ADVENT_2020\input\day3.txt",'r').read().replace(".","0").replace("#","1").splitlines()
# Read file. Convert symbols to binary tree/no tree. Plan to sum all 1 values encountered. 
inp1 = [list(inp0[i]*(round(len(inp0)*3/len(inp0[1]))+1)) for i in range(len(inp0))]
# Needed to repeat pattern the necessary length: n*31 chars = 3*323 map rows, round n up
# From here final step is split long string to char, then convert str chars to int:
inp = [] 
for i in range(len(inp1)): # Open up the 
   row = [int(inp1[i][j]) for j in range(len(inp1[i]))]
   inp.append(row)
del inp0, inp1, row, i
# Input processing done

# Puzzle 1---------------------------------------------------------------------
# Task: Tobogg starts (0,0) moves right 3 down 1; count ONLY trees enc on vertices
trees = 0
a = 0
b = 0
for a in range(len(inp)):
    trees = trees + inp[a][b] # Not a range, just an individual entry
    a = a + 1
    b = b + 3

s1 = trees
# Correct! Took a couple goofs on this one. Slicing vs. indexing vs. looping.
t1 = time.time()

# Puzzle 2---------------------------------------------------------------------
# Task: Do similar for other path combinations, then multiply tree counts together.
trees = []
paths = [[1,1],[3,1],[5,1],[7,1],[1,2]]
for p in range(len(paths)):
    x,y = paths[p]
    a,b,t = [0,0,0]
    for i in range(len(inp)):
        t = t + inp[i+(y-a)][b] # Add for each tree encountered at a step.
        a = a + x
        b = b + y
    # Add tree count t to trees count? End up with five entries?
# Then multiple each path's result?
# Going to need to fix length of input map (see below) first...
'''
Realizing now I didn't make this flexible enough. Need to repopulate map
to accommodate higher sloped paths (more rightward motion).
- Bring map sizing into loop with "paths"? it becomes a multiple of the rows you need, right?

Also tricky with the loops. How to simplify?
- 

Merry Christmas! 
'''

s2 = sum(trees)
# Result.
t2 = time.time()
d3_t = t2-t0 # Log 

'''
Day 3 Drawing Board

This can be simplified I think just by selecting 4 cells per row and adding, 
then running for all rows (323). This is just a cascading pattern if you draw
it out.
(0,0) + (0,1) + (0,2) + (0,3) + (1,3) + (1,4) ... becomes
0: (0,0) + (0,1) + (0,2) + (0,3) 
1: (1,3) + (1,4) + (1,5) + (1,6) 
2: (1,7) + (1,8) + (1,9) + (1,10)
... etc.

# Missed the chance to zip on an earlier day. Allows for multidim symmetric steps
for a,b in zip(len(inp), len(inp[0])): # a = 0:323 rows, b = 0:992 items max
    [func]

# This was my approach when I thought we counted ALL entried in EACH of the cells
# the tobb passes. Not the case, only count the end of the L-shaped steps. 
# Traverse 3 col per row, 323 rows total, need to pop 323*3 across where each row is 31
ct = 0
b = 0
for a in range(len(inp)):
    path = inp[a][b:b+4]
    tree = sum(path)
    b = b + 3
    ct = ct + tree
# Oops.

'''
#%% DAY 4
# Setup 
import time
import pandas as pd
t0 = time.time()

# Input 
inp = open("C:\Python37\Projects\ADVENT_2020\input\day4.txt",'r').read()

# Puzzle 1---------------------------------------------------------------------
# Task: Count valid passports, excluding North Pole citizens
# Valid are those that contain all fields save cid, which is optional.



s1 = []
# Result. 
t1 = time.time()

# Puzzle 2---------------------------------------------------------------------
# Task: 


s2 = []
# Result.
t2 = time.time()
d4_t = t2-t0 # Log 

'''
Day 4 Drawing Board
'''
#%% DAY 5
# Setup 
import time
import pandas as pd
t0 = time.time()

# Input 
inp = open("C:\Python37\Projects\ADVENT_2020\input\day5.txt",'r').read()

# Puzzle 1---------------------------------------------------------------------
# Task: 


s1 = []
# Result. 
t1 = time.time()

# Puzzle 2---------------------------------------------------------------------
# Task: 


s2 = []
# Result.
t2 = time.time()
d5_t = t2-t0 # Log 

'''
Day 5 Drawing Board
'''
