import numpy as np
from CoinToss import CoinToss

"""-------------------------------------------Inherited Variables--------------------------------------------------------------------

   - Sample Space:                            Ω = {ωₖ | for k=1,...,∞}                                       = self.SampleSpace
   
   - Random Variable :                      X: ω-> ( {-1,1} valued sequences )                      = self.RandVariable
                                           ...written as: X(ω) = (ζ₁ , ζ₂ , ζ ₃ ,...)  = (-1, 1, -1, ...)
                                           
-------------------------------------------------------------------------------------------------------------------------------------"""
"""---------------------------------------RandomWalk Object Variables-----------------------------------------------------------

    - States:                                     S = ( ζ ₁ , ζ ₁ +  ζ ₂ , ζ ₁ +  ζ₂  + ζ ₃ ,... )                  = self.States 
    
    - Moving Averages:                    Avgs = ( S1, (S1+S2)/2, (S1+S2+S3)/3 ,... )           = self.Avgs

--------------------------------------------------------------------------------------------------------------------------------------"""

#  Inherits from the CoinToss class
class RandomWalk(CoinToss):
    
    def __init__(self, Length = 250):
        super().__init__()

        self.States = None
        self.Avgs = list()
        self.Length = Length
        self.addSample(Length-1)
        self.calculateStates()
        

    #  Changes the default length of the Random Walk.
    def setLength(self, Length: int):
        self.Length = Length
        
   # Calculates the Random walk 
    def calculateStates(self):
        Sum = 0
        State = []
        State.append(Sum)
            
        for k in self.RandVariables[0]:
            Sum += k
            State.append(Sum)
        self.States = np.array(State)


    #  Calculates the Moving average for each set of States
    def movingAvgState(self):
        N = len(self.States)

        for i in range(N):
            Sum = 0
            Avg = []
            X = self.States[i]
            
            for j in range(len(X)):
                Sum += X[j]
                Avg.append(Sum/(j+1))
            self.Avgs.append(Avg)

    def getStateAt(self, n):
        if n <= self.Length:
            return self.States[n]
        
        
        
            
            
            
