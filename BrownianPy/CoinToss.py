import numpy as np
import Maps

class CoinToss():
    
    """ --------------------------------------- Class Variables------------------------------------------------------------------------
    
    Sample Space:                            Ω = {ωₖ | for k=1,...,∞} = self.SampleSpace
    Samples :                                ω = (T,H,H,T,...) = elements of Ω
    
    IID Random Variable :                    ζ : {H, T} -> {1,-1}  = self.zeta
    
    Random Variable :                        X: ω-> {sequences of {-1,1}}  (elements of self.RandVariables)
                                                                       X(ω) = (ζ₁ , ζ₂ , ζ ₃ ,...)  = (-1, 1, -1, ...)   
    ---------------------------------------------------------------------------------------------------------------------------------"""
    
    def __init__(self):
        self.zeta = dict({'H':1, 'T':-1})
        self.RandVariables = list()
        self.SampleSpace = list()
   
    #  returns a {-1,1} valued sequence
    def RandVariable(self, ω):
        return [self.zeta[ω[i]] for i in range(len(list(ω)))]
    
    #  Add individual samples ω having length = Length to Ω 
    def addSample(self, Length: int):
        fArray = Maps.randFloats(Length)
        ω = [Maps.float2HT(fArray[i]) for i in range(Length)]
        self.SampleSpace.append(ω)
        self.RandVariables.append(self.RandVariable(ω))
    
    # Add samples of length sizes = [a,b,c,...] to the Sample space  Ω 
    def addSamples(self, sizes):
        events = [self.addSample(size) for size in sizes]
        for event in events:
            if not event == None:
                self.SampleSpace.append(event)
