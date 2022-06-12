"""
This was a file to scrape in bulk all inputs and puzzle premises for past years.
Wanted to take it offline. Should only be run once. Pauses are built in. 
"""
import os
import time
import requests
import numpy as np

base_url = r'https://adventofcode.com' 
years = [2019,2020,2021]

with open('aoc_session_id.txt') as f: # Need session_id, lasts 1 year from creation
    session_id = f.readlines()[0]

for year in years:
    for n in np.arange(1,25,1):
        print("Starting year " + str(year) + ", day " + str(n) + ".")
        puzzle = base_url + r'/' + str(year) + r'/day/' + str(n)

        if os.path.exists(str(year) + "/premise/day" + str(n) + ".txt") is False: 
            puzzle_premise = requests.get(puzzle, cookies={'session':session_id})
            with open(str(year)+"/premise/day"+str(n)+".txt", "w", encoding="utf-8") as f:
                f.write(puzzle_premise.text) # Writes puzzle details/instructions to text file
            time.sleep(15) # Courtesy sleep per request of @ericwastl
        
        if os.path.exists(str(year) + "/input/day" + str(n) + ".txt") is False: 
            puzzle_input = requests.get(puzzle + r'/input', cookies={'session':session_id}) # Rejected, need to log in
            with open(str(year)+"/input/day"+str(n)+".txt", "w", encoding="utf-8") as f:
                f.write(puzzle_input.text)
            time.sleep(15) # Courtesy sleep per request of @ericwastl
        
        print("Done with day " + str(n) + ", on to the next.")
