import itertools
from tqdm import tqdm
from collections import Counter
# from arrs import *
import math
import numpy as np
from sympy import primefactors, sieve
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import random
import matplotlib.pyplot as plt

import networkx as nx


from itertools import chain, combinations, combinations_with_replacement


def eval_poly(coef, n, mod):
    n = int(n)
    l = len(coef)
    out = 0
    for i in range(l):
        out += (n**i)*coef[i]

    if out < 0:
        out +=  (2  + abs(out)//mod)*mod

    out = out%mod

    return out 

def number_of_sol(p, mod):
    c = 0
    for i in range(mod):
        if eval_poly(p, i, mod) == 0:
            c +=1 
    return c

def sum_of_number_ofsol(p):
    s = sum([number_of_sol(p, i) for i in range(2, 145)])
    return s

def eval_on_mods(p, upto):
    return [number_of_sol(p, i) for i in range(2, upto)]

def find_smallest_sum():
    minp = []
    minv = 1000
    coefs = list(range(0, 145))

    for t in itertools.product(coefs, coefs):
        #t = t[::-1]

        if  t[-1] <= 0 :
            continue

        s = sum_of_number_ofsol(t)
        if s < minv:
            minv = s
            minp = t
            print(minv, minp)


def find_biggest_sum():
    maxp = []
    maxv = 1000
    coefs = list(range(0, 100))

    for t in itertools.product(coefs, coefs, coefs):

        if  t[2] <= 0 :
            continue

        s = sum_of_number_ofsol(t)
        if s > maxv:
            maxv = s
            maxp = t
            print(maxv, maxp)

def vizualize_poly_num():
    p = [-1, -1, 1, 1, 3]
    maxv = 40

    c = np.zeros((maxv, maxv))
    

    for i in tqdm(range(maxv)):
        for j in range(maxv):
            p[1] = i - maxv//2
            p[2] = j - maxv//2
            c[i, j] = sum_of_number_ofsol(p)

    plt.figure(num = None)

    plt.axis('off')

    plot = plt.imshow(c, cmap = 'hot')

    plt.show()
    plt.close()

if __name__ == "__main__":
    find_smallest_sum()
    #find_biggest_sum()

    # p = (13, -19, -20, 1)
    # p2 = (23, -35, 1)
    # # p3  = (41, 1, 1)


    # arr = eval_on_mods(p2, 1_000)
    # print(sum(arr))

    







