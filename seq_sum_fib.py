import itertools
#from tqdm import tqdm
from collections import Counter

#from arrs import *
import numpy as np
import random
import math
#import ctypes
from sympy import primefactors, sieve
from sympy.ntheory import qs
from sympy.ntheory.continued_fraction import continued_fraction
from tqdm import tqdm 
from sympy.ntheory.continued_fraction import continued_fraction_reduce
from sympy import sympify
from fractions import Fraction
from sympy import symbols, fraction, UnevaluatedExpr

base = 10

sieve._reset() # this line for doctest only
sieve.extend_to_no(80_000)
primes = sieve._list 

def first_div_ret(n):
    for i in primes:
        if n % i == 0:
            return i 
    return 0

def forfor(a):
    return [item for sublist in a for item in sublist]

def in_base_10(n):
    reverse_bits = []
    while n > 0:
        reverse_bits.append(n % base)
        n //= base
    return reverse_bits  #[::-1]

def from_base_10(s):
    t = 0

    for c, v in enumerate(s):
        t += (base**c)*v

    return t


def flip_10_seq(n, it):
    out = [n]

    for it in range(it):

        s = in_base_10(n)
        d = first_div_ret(n)
        if d == 0:
            break

        #print(s)

        if d > 10**5:
            break

        if d  >= len(s):
            s = s + [0]*(d -len(s) +2  )
        #print(s, d)

        s[d] = (s[d] + d*2)%base

        n = from_base_10(s)

        if  n > 10**150:
            break

        out.append(n)

        if findcycle(out) != []:
            break

    return out


def findcycle(c):
    t = []
    for i in c:
        if i not in t:
            t.append(i)
        else:
            t.append(i)

            return t[t.index(i):]
    return []

def list_of_sum(c):
    out = []
    for i in range(1, len(c)):
        s = c[i] - c[i-1]
        out.append( math.ceil(math.log(abs(s), base)*(s/abs(s))))
    return out




if __name__ == "__main__":

    for n in [ 10]:
        base = n
        chek_trivial_loops = 1

        a = []
        typeout = []
        outlens = []
        for i in tqdm(range(0, 10_000, 1)):
            if i % base == 0: 
                if not chek_trivial_loops:
                    continue

            c = flip_10_seq(i, 8000)
            c = findcycle(c)
            cdiv = [first_div_ret(j) for j in c]
            #sdiv = list_of_sum(c)

            if c != [] and (len(cdiv), set(cdiv)) not in typeout:
                #print('\n\n')

                print(c, i,  set(cdiv), len(cdiv))
                #print(c[0], len(cdiv), set(cdiv))

                outlens.append(len(c))

                typeout.append((len(cdiv), set(cdiv)))

        print(n , sorted(outlens), len(set(outlens)))


    arr11 = [133, 133, 155, 155, 177, 177, 199, 265, 287, 331, 353, 375, 419, 727]
