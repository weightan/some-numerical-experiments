
import itertools
#from tqdm import tqdm
from collections import Counter

#from arrs import *
import numpy as np
#import random
import math
#import ctypes
from sympy import primefactors, sieve
from sympy.ntheory import qs

from tqdm import tqdm 

sieve._reset() # this line for doctest only
sieve.extend_to_no(40_000)
primes = sieve._list 


def num_tostr(n, length):
    s = format(n, 'b')
    #print(s)
    s = s.zfill(length)
    return s


def flip_bit(s, nbit):
    #nbit -=1
    if len(s) < nbit:
        return s

    s = list(s)[::-1]

    if s[nbit] == '0':
        s[nbit] = '1'
    else:
        s[nbit] = '0'

    return ''.join(s[::-1])


def flip_seq(start, nterms):
    arr = [start]
    current = start

    for i in range(nterms):

        #print(1)
        pf = first_div_ret(current)
        

        if pf  == False:
            break

        s = num_tostr(current, pf + 1)

        
        s = flip_bit(s, pf)

        current = int(s, 2)

        arr = arr + [current]

        if current > 10**3000000:
            break
        if findcycle(arr) != []:
            return arr


    return arr


def findcycle(c):
    t = []
    for i in c:
        if i not in t:
            t.append(i)
        else:
            t.append(i)

            return t[t.index(i):]
    return []



def run():

    cycl_temp = []
    pa = []
    cr = []
    #13, 43,115,123,139, 151,159

    for i in [13, 43, 115, 123, 139, 151,159] : #range(3, 400, 2):

        c = flip_seq(i, 10_000)

        cy = findcycle(c)
        print(i, len(c) , len(cy))

        print_arr_as_powers(c)

        if len(cy) >= 7:
            cycl_temp = cycl_temp +  [cy]
            pa.append((i, len(cy)))

    for i in pa:
        print(i)

    t = []


def print_as_powers(n):
    outs = ''

    s = format(n, 'b')
    s = list(s[::-1])


    for i in range( len(s)):

        if s[i] == '1':
            outs = outs + f' + 2**({i})'

    return outs[2:]

def print_arr_as_powers(arr):
    s = ''
    for i in arr:
        s = s  + print_as_powers(i) + ', \n'

    print(s)


if __name__ == "__main__":
    #run()

    run()


