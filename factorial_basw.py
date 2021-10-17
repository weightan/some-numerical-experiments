import numpy as np
import itertools
import math
from tqdm import tqdm
# import scipy
# import functools
# import operator
from sympy import primefactors, sieve

import random
from sympy import *

from itertools import combinations
from itertools import permutations


def to_factorial_s(n):
    out = []
    c = 1
    if n == 0:
        return [0]

    while n > 0:
        out.append(n%c)
        n = n//c 
        c +=1

    
    return out #[::-1]

def from_fact_s(s):
    #s = s[::-1]
    out = 0
    for i in range(len(s)):
        out  = out + s[i]*math.factorial(i)
    return out

from sympy import sieve

def run():

    sieve._reset() 
    sieve.extend(2_000_000)

    primes = sieve._list

    #a = to_factorial_s(463)

    main_arr = []
    out = []

    for i in tqdm(primes):

        main_arr.append( to_factorial_s(i) )


    mdt = 0

    for i in tqdm(main_arr):
        h = 0
        dt = 0
        for j in range(len(i)):
            if h == 1:
                break
        
            for t in range(0, j+1):
                c = i.copy()
                c[j] = t

                #dt += 1

                if c in main_arr  and c != i :
                    h = 1
                    #print(c, i)
                    break

        # if dt > mdt:
        #     print(dt, i)
        #     mdt = dt

        if h ==0:
            print(i)
            out.append(i)

    print(out)

def trim_z(l):
    s =[]
    c = 0
    if all(i == 0 for i in l) :
            return [0]

    for i in range(len(l)):
        if l[i] != 0:
            c = 1

        if c == 1:
            s.append(l[i])

        
    return s
    



def run_squares():

    sqar = [i**2 for i in range(0, 10**6)]

    #a = to_factorial_s(463)

    main_arr = []
    out = []

    for i in tqdm(sqar):

        main_arr.append( to_factorial_s(i) )


    mdt = 0

    for i in main_arr:
        h = 0
        dt = 0
        for j in range(len(i)):
            if h == 1:
                break
        
            for t in range(0, len(i)):
                c = i.copy()
                c[j] = t
                c = trim_z(c[::-1])[::-1]
                #dt += 1

                if c in main_arr  and c != i :
                    h = 1
                    #print(c, i)
                    break

        # if dt > mdt:
        #     print(dt, i)
        #     mdt = dt

        if h ==0:
            print(i, from_fact_s(i))
            out.append( round((from_fact_s(i))**(1/2)) )
            if len(out) > 120:
                break

    print(out)



def check_near(s):

    for i in range(len(s)):
        for j in range(0, len(s)):
            cs = s.copy()
            cs[i] = j
            if cs != s:
                c = isprime(from_fact_s(cs))
            if c == 1:
                return 0
    return 1
                



if __name__ == "__main__":

    run_squares()
    
    #print(to_factorial_s(4))

    

    # for i in b:
    #     if i not in z:
    #         print(i)

    # for i in z:
    #     if i not in b:
    #         print(i)

    print(to_factorial_s(24))

    #print(trim_z([0, 0, 0, 0, 1, 1,0][::-1])[::-1])
