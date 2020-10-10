import numpy as np
import string

def float2HT(x: float):
    if 0 <= x and x < 0.5:
        return "T"
    
    elif 0.5 <= x and x <= 1:
        return "H"

    elif x < 0 or x > 1:
        print('input must be in [0,1]')

def randFloats(length: int):
    return np.random.rand(length)

def subscr(n: int):
    SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    return str(n).translate(SUB)
