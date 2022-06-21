# Plot
from matplotlib import pyplot as plt

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

def paths_plot(patha,pathb):
    plt.grid()
    plt.plot(patha[:,0], patha[:,1], marker="o", markersize=1, markeredgecolor="green", markerfacecolor="green")
    plt.plot(pathb[:,0], pathb[:,1], marker="o", markersize=1, markeredgecolor="blue", markerfacecolor="blue")
    plt.show()
    return 
