import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.ticker import FormatStrFormatter
from matplotlib.ticker import PercentFormatter

x_vals = []
y_vals = []

index = count()
print("Opening graph...")


def animate(i):
    datafile = open("data.txt", "r")
    inputdata = str(datafile.read())
    datafile.close()

    a0 = []
    a1 = []

    inputdata = inputdata.split("\n")
    for i in range(len(inputdata)):
        inputdata[i] = inputdata[i].split(",")
        a0.append(inputdata[i][0])
        a1.append(inputdata[i][1])
    
    a1 = a1[::-1]
    a1 = list(map(float, a1))
    a0 = a0[::-1]

    #Capitalize first letter
    for i in range(len(a0)):
        a0[i] = a0[i][0].upper() + a0[i][1:]

    plt.cla() 
    plt.legend("")
    plt.style.use('fast')
    #plt.plot(x, y1, label="", linewidth=5)
    plt.barh(a0, a1, color="#8C0800")
    plt.xlim(min(a1) - 1, max(a1) + 0.2)
    #plt.ylabel("Winrate")
    #plt.xlabel("Match number")
    #plt.gca().yaxis.set_major_formatter(PercentFormatter(xmax=1))
    plt.tight_layout()

ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()


"""
f = open("data.txt", "r")
test = f.read()
print(test)
f.close()
"""
