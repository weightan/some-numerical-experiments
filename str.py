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


def forfor(a):
    return [item for sublist in a for item in sublist]

# 735 [3, 5, 7]
# 3792 [2, 3, 79]
# 1341275 [5, 13, 4127]


if __name__ == "__main__":
    out = []
    for i in tqdm(range(1_341_275, 10_000_000)):
        s = list(str(i))

        s3 = forfor([ list(str(j)) for j  in primefactors(i)    ])

        if len(primefactors(i)) != 1 and sorted(s) == sorted(s3)  :

            strd = [ str(j) for j  in primefactors(i)    ]

            for p in itertools.permutations(strd):

                strong = ''
                for item in p:
                    strong = strong + item

                if strong == str(i):
                    out.append((i, primefactors(i)))
                    print(i, primefactors(i))
    print(out)

