import numpy as np
import matplotlib.pyplot as plt
from CoinToss import CoinToss


"""-------------------------------------------Inherited Variables--------------------------------------------------------------------

   - Sample Space:                            Ω = {ωₖ | for k=1,...,∞}                                       = self.SampleSpace
   
   - Random Variable :                      X: ω-> ( {-1,1} valued sequences )                      = self.RandVariable
                                           ...written as: X(ω) = (ζ₁ , ζ₂ , ζ ₃ ,...)  = (-1, 1, -1, ...)
                                           
-------------------------------------------------------------------------------------------------------------------------------------"""
"""---------------------------------------RandomWalk Object Variables-----------------------------------------------------------

    - States:                                     S = ( ζ ₁ , ζ ₁ +  ζ ₂ , ζ ₁ +  ζ₂  + ζ ₃ ,... )                  = self.States
    
    - Length:                                    Number of steps in Random Walk.                    = self.Length

--------------------------------------------------------------------------------------------------------------------------------------"""

#  Inherits from the CoinToss class
class RandomWalk(CoinToss):
    
    def __init__(self, Length = 500):
        super().__init__()

        self.States = None
        self.Length = Length
        self.addSample(Length-1)
        self.calculateStates()
        
   # Calculates the Random walk 
    def calculateStates(self):
        Sum = 0
        State = []
        State.append(Sum)
            
        for k in self.RandVariables[0]:
            Sum += k
            State.append(Sum)
        self.States = np.array(State)

    # Returns State
    def getStateAt(self, n):
        if n <= self.Length:
            return self.States[n]
    
   # Plots the Random Walk
    def plot(self):
        plt.style.use('dark_background')
        fig, ax = plt.subplots(figsize=(12,9))
        ax.set_xlim(0,self.Length)
        ax.set_ylim(np.min(self.States)-0.5, np.max(self.States)+0.5)
        string = "Random Walk with " +str(self.Length) + " steps"
        ax.title.set_text(string)

        if self.Length > 501:
            size = 1.5
        else:
            size = 3.0
        if self.Length > 1000:
            ax.plot(self.States, color = 'white',
                    linestyle = '-', marker = 'o',
                    markersize = size, markerfacecolor = 'red', markeredgecolor='red',
                   lw = 0.05)
        else:
            ax.plot(self.States, color = 'white', lw = 0.65)
            
        ax.set_xlabel('Time Step (n)')
        ax.set_ylabel('State')
        plt.show()
