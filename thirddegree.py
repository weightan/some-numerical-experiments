import numpy as np
import itertools
import math
from tqdm import tqdm
import scipy

import random
from sympy import *


from numba import jit


def eval_eq_mod_third(V, m):
    a = int(V[0])
    b = int(V[1])
    c = int(V[2])

    # if not less:
    #     x = x%m
    #     y = y%m
    #     z = z%m

    a_c = (a*a*a)%m
    b_c = (b*b*b)%m
    c_c = (c*c*c)%m
    const_q = (97969)%m

    return abs(a_c + b_c - const_q*c_c) %m == 0

def make_list_of_primes(n):
    primes = []

    for i in range(2, n + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i%j == 0:
                break
        else:
            primes.append(i)

    return primes


def ex_count():
    primes = [17*19*2]
    pars_m_c = []

    for m, it in tqdm(zip(primes, range(len(primes)))  ):
        temp = 0

        rem =[i for i in range(m)]

        for i in  tqdm(itertools.product(rem, rem, rem) ):
            d = eval_eq_mod_third(i, m)
            if d :
                
                temp = 1 + temp

        pars_m_c.append((m, temp))
        #print('mod : ', m, ' count of fitting: ', temp, 'percent: ', temp/(m**3))

    pm = min(pars_m_c, key = lambda x:  x[1]/( x[0]**3))
    print('\n')
    print('mod : ', pm[0], ' count of fitting: ', pm[1], 'percent: ', pm[1]/(pm[0]**3))


    


def ex2():
    x, y, z, t = symbols('x y z t')
    k, m, n = symbols('k m n', integer=True)
    f, g, h = symbols('f g h', cls=Function)

    primes = [133]#make_list_of_primes(6)
    points = []

    for m, it in zip(primes, range(len(primes))):
        temp = []

        rem =[i for i in range(m)]

        for i in  itertools.product(rem, rem, rem) :
            d = eval_eq_mod_third(i, m)
            if d :
                count = 1+ count
                temp.append(i)

        points.append(temp)


    for i, prime in zip(points, primes):
        rp = []

        for e in i:
            if e[2] not in rp:
                rp.append(e[2])

        i = sorted(i, key = lambda k: k[2])

        i2 = []
        for r in i:
            if r not in i2 and (r[1], r[0], r[2]) not in i2:
                i2.append(r)

        print(prime, len(i2), len(i2)/(prime**3))

        for j in i2 :
            print(j)


        print(sorted(rp))


if __name__ == "__main__":
    ex_count()
    #print(313**2)

