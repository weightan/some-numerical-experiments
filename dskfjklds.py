import itertools
from tqdm import tqdm
from collections import Counter
import math
from sympy import primefactors, sieve
import matplotlib.pyplot as plt

from itertools import chain, combinations, combinations_with_replacement
import functools 


@functools.lru_cache(maxsize=1024)
def a(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 3

    if n % 4 == 0:
        return a(n/4)
    else:
        return a(n - math.floor(n/4))



if __name__ == "__main__":
    print([a(i) for i in range(1, 100)])
