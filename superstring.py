
import itertools
from tqdm import tqdm
from collections import Counter
from arrs import *

import random
import math
import ctypes



from typing import Iterable, Union, Any

def de_bruijn(k: Union[Iterable[Any], int], n: int) -> str:
    """de Bruijn sequence for alphabet k
    and subsequences of length n.
    """
    # Two kinds of alphabet input: an integer expands
    # to a list of integers as the alphabet..
    if isinstance(k, int):
        alphabet = list(map(str, range(k)))
    else:
        # While any sort of list becomes used as it is
        alphabet = k
        k = len(k)

    a = [0] * k * n
    sequence = []

    def db(t, p):
        if t > n:
            if n % p == 0:
                sequence.extend(a[1 : p + 1])
        else:
            a[t] = a[t - p]
            db(t + 1, p)
            for j in range(a[t - p] + 1, k):
                a[t] = j
                db(t + 1, t)

    db(1, 1)
    return "".join(alphabet[i] for i in sequence)

def make_list_of_bstrings(length):
    n = 2**length
    arr = []

    for i in range(n):
        a = format(i, 'b')
        a = a.zfill(length)
        arr.append(a)

    return arr


def summ_strings_min(a, b):
    btwo = str(b)

    for i in range(len(b)  , -1, -1):

        if a[ len(a) - i : ]  == b[: i]:

            #print( '_____' + a[ len(a) - i:] )
            #print('_____' + b[ i: ] )

            return a[  : len(a) - i ] +  b

    return a + b


def naive_rec_superstring(arr, this_string = '', n = 0):
    supstr_max = ''
    supstr_max_len  = 100000

    if len(arr) == 0:

        return this_string

    for i in range(len(arr)):
 
        #print(i)
 
        this_string_new = summ_strings_min(this_string, arr[i])

        another_list = arr.copy()
        another_list.remove(arr[i])

        supstr  =  naive_rec_superstring(another_list, this_string_new, n + 1)

        if  len(supstr ) < supstr_max_len :
            if n  == 1:
                print(supstr, n)

            supstr_max_len =  len(supstr)
            supstr_max = supstr


    
    return supstr_max

    
def superstring_random(ar, iters):

    min_sup = ''
    min_sup_len = 619

    for i in tqdm(range(iters)):
        currentArr = ar.copy()
        random.shuffle(currentArr)
        sup = ''
        c = 1

        for ch in currentArr:
            sup = summ_strings_min(sup, ch)

            if len(sup) >= min_sup_len:
                c = 0
                break

        if   c and len(sup) < min_sup_len :
            min_sup = sup
            min_sup_len = len(sup)

    return min_sup


def super_combinations(ar, iters):

    min_sup = ''
    min_sup_len = 619

    for i in tqdm(range(iters)):
        currentArr = ar.copy()
        random.shuffle(currentArr)
        sup = ''
        c = 1

        for ch in currentArr:
            sup = summ_strings_min(sup, ch)

            if len(sup) >= min_sup_len:
                c = 0
                break

        if   c and len(sup) < min_sup_len :
            min_sup = sup
            min_sup_len = len(sup)

    return min_sup


def ordered_supstr():
    n = 4
    copy          = ctypes.pythonapi._PyUnicode_Copy
    copy.argtypes = [ctypes.py_object]
    copy.restype  = ctypes.py_object

    ar = make_list_of_bstrings(n)
    print(ar, len(ar))
    sup = naive_rec_superstring(ar)

    print(sup, len(sup), len(sup)/(n*len(ar)))



def chaos_supstr():

    n = 7

    ar = make_list_of_bstrings(n)
    print(ar, len(ar))

    sup = superstring_random(ar, 10**6)

    print(sup, len(sup), len(sup)/(n*len(ar)))


def chaos_sup_comb():
    
    
    n = 2

    ar = list(itertools.combinations('12345', n))
    ar = [''.join(i) for i in ar]
    print(ar, len(ar))

    sup = naive_rec_superstring(ar)

    print(sup, len(sup), len(sup)/(n*len(ar)))



if __name__ == "__main__":
    #chaos_supstr()
    # for i in range(2, 80):
    #     a = de_bruijn(2, i)

    #     print( len(a), i)

    chaos_sup_comb()


    

    

    
    

    