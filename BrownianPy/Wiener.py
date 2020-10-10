from RandomWalk import RandomWalk as rw
from Maps import subscr
import numpy as np
import math
import matplotlib.pyplot as plt


class WienerVar():

    def __init__(self, t=1, Length = 250):
        self.S = rw(Length)
        self.Length = Length
        self.t = t
        self.calculateStates()

    def calculateStates(self):
        states = list()
        for i in range(len(self.S.States)):
            N = math.floor(i*self.t)
            states.append( self.S.getStateAt(N) / math.sqrt( (i+1) ) )
        self.States = np.array(states)

    def getStateAt(self, n):
        if n <= self.Length:
            return self.States[n]

    def plot(self):
        plt.style.use('dark_background')
        fig, ax = plt.subplots(figsize=(12,9))
        ax.set_xlim(0,1)
        ax.set_ylim(np.min(self.States)-0.5, np.max(self.States)+0.5)
        string = "W" + subscr(self.t)
        ax.title.set_text(string)

        if self.Length > 500:
            size = 1.5
        else:
            size = 3.0
        if self.Length < 1000:
            ax.plot(np.linspace(0,1,self.Length), self.States, color = 'white',
                    linestyle = '-', marker = 'o',
                    markersize = size, markerfacecolor = 'red', markeredgecolor='red',
                   lw = 0.05)
        else:
            ax.plot(np.linspace(0,1,self.Length), self.States, color = 'white', lw = 0.65)
            
        ax.set_xlabel('Time Step (n)')
        ax.set_ylabel('State')
        plt.show()
