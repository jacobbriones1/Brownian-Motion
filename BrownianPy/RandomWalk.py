import numpy as np
from CoinToss import CoinToss

"""-------------------------------------------Inherited Variables--------------------------------------------------------------------

    Sample Space:                            Ω = {ωₖ | for k=1,...,∞} = self.SampleSpace                                                        
    Samples :                                    ω = (T,H,H,T,...) = elements of Ω             
    
    IID Random Variable :                    ζ : {H, T} -> {1,-1}  = self.zeta
    
    Random Variable :                        X: ω-> {sequences of {-1,1}}  (elements of self.RandVariables)
                                                                       X(ω) = (ζ₁ , ζ₂ , ζ₃ ,...)  = (-1, 1, -1, ...)   
-------------------------------------------------------------------------------------------------------------------------------------"""

 """---------------------------------------RandomWalk Object Variables----------------------------------------------------------

    States:                                 S = ( ζ₁ , ζ₁ +  ζ₂ , ζ₁ +  ζ₂  + ζ₃ ,...) = self.States 
    
    Moving Averages:                        Avgs = ( S1, (S1+S2)/2, (S1+S2+S3)/3 ,... ) = self.Avgs

--------------------------------------------------------------------------------------------------------------------------------------"""

#  Inherits from the CoinToss class
class RandomWalk(CoinToss):
    
    def __init__(self):
        super().__init__()
        self.States = list()
        self.Avgs = list()

    #  **kwards should be a list consisting of the number of Steps for each Random Walk.
    #        can be a single number. If nothing is entered, it will create a defauly sample of
    #        length 250,
    def populate(self, **kwargs):
        if len(kwargs) != 0:
            N = list(kwargs.values())
            if len(kwargs.values()) == 1:
                self.addSample(N[0])
            else:
                self.addSamples(N)    
        else:
            self.addSample(250)
            

   # Calculates the Random walk for all Samples
    def calculateStates(self):
        for var in self.RandVariables:
            Sum, State = 0, []
            for k in var:
                Sum += k
                State.append(Sum)
        self.States.append(State)
        

    #  Calculates the Moving average for each set of States
    def movingAvgState(self):
        N = len(self.States)
        for i in range(N):
            Sum, Avg = 0, []
            X = self.States[i]
            for j in range(len(X)):
                Sum += X[j]
                Avg.append(Sum/(j+1))
            self.Avgs.append(Avg)
