import numpy as np
from collections import Counter

# Helper Function: Maps [0,1] to {H,T}
def float2HT(x):
    if x < 0 or x > 1:
        print('Input must be a random number in the range [0,1]')
        return
    elif 0 <= x and x <0.5:
        return 'T'
    else:
        return 'H'

class CoinToss:
    def __init__(self, maxOutcomes = 10):
        self.maxOutcomes = maxOutcomes
        self.map = dict({'H':1, 'T':0})
        self.inverseMap = dict({1:'H', 0:'T'})
        self.zeta = None
        
        if maxOutcomes != None:
            randNums = np.random.rand(maxOutcomes)
            self.Outcomes= [float2HT(x) for x in randNums]

    def setMaxOutcomes(N):
        self.maxOutcomes = N
        randNums = np.random.rand(N)
        self.Outcomes= [float2HT(x) for x in randNums]

    # Maps {H,T} to {-1,1}
    def PlusMinusHT(self):
        self.zeta = [self.map[X] for X in self.Outcomes]
        return self.zeta

    def frequency(self):
        return dict(Counter(self.Outcomes))
