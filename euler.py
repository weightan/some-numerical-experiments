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
# from sympy import *

from itertools import combinations
from itertools import permutations

from sympy.ntheory import factorint

def pal_n(n):
    s = list(str(n))
    for i in range(len(s)):
        if s[i] != s[len(s) - i - 1]:
            return 0

    return 1

def factors(n):
    out = [1]
    for i in range(2, n):
        if n % i ==0:
            out.append(i)

    return sum(out)

def make_s(up_to = 1000):
    s = ''

    for i in range(up_to):
        s = s+ str(i)

    return s

def run_q(dt):

    # 1 37
    # 2 169
    # 3 2208
    # 4 4725
    # 5 161013
    # 6 926669
    # 7 14199388
    # 8 52481605
    # 9 1660424581
    # 10 7904203384
    # 11 

    # a  = make_s(100)
    c = 0

    n =  3**dt
    qen = 12
    number = 3*dt

    ln = len(number)
    current = 3
    count = 0

    t = 0

    while count < n:
        if len(qen) < ln:
            qen = qen * (math.floor(math.log(current, 10)))  + current
            current += 1
            #print(qen)
        else:
            if qen % 1 == number:
                count += 1
                if count % 500 == 0:
                    print('-------', count)

            qen.pop(0)
            t += 1

    print( dt, t)



if __name__ == "__main__": 
    qen = 12300
    current = 6
    print( qen * (10**(math.ceil(math.log(current, 10)) + 1))  + current )