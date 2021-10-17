import numpy as np
import itertools
import math
from tqdm import tqdm
# import scipy
# import functools
# import operator
from sympy import primefactors, sieve
import matplotlib.pyplot as plt
import random
from sympy import *

from itertools import combinations
from itertools import permutations
base = 2**14 + 1
dots = []
maxd = 0
maxp = 0

def run():
    out = []
    maxd = 0
    maxp = 0

    for i in tqdm(range(1, base)):
        if format(i, 'b') in format(base**i, 'b'):
            out.append((i))
            #print(str(base ** i))

    #print( base, len(out)/ base)
    #dots.append(len(out)/ base)

    return out
       

if __name__ == "__main__":
   
    a = run()

    for i in range(0, base):
        if i not in a:
            print(i)


    # print(maxp, maxb)

    # plt.plot(dots)
    # plt.ylabel('some numbers')
    # plt.show()

