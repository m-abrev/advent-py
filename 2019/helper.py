# Plot
from matplotlib import pyplot as plt

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

## Day 3
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

def paths_plot(patha,pathb):
    plt.grid()
    plt.plot(patha[:,0], patha[:,1], marker="o", markersize=1, markeredgecolor="green", markerfacecolor="green")
    plt.plot(pathb[:,0], pathb[:,1], marker="o", markersize=1, markeredgecolor="blue", markerfacecolor="blue")
    plt.show()
    return 
