import itertools
from tqdm import tqdm
from collections import Counter
import math
from sympy import primefactors, sieve
import matplotlib.pyplot as plt

from itertools import chain, combinations, combinations_with_replacement
import functools 

m = 970
@functools.lru_cache(maxsize=10024)
def a(n):
    if n < m:
        return (int(n)**2) % m
    if n % m == 0:
        return a(n/m)
    else:
        return a(n - math.floor(n/m))



if __name__ == "__main__":
    s = [a(i) for i in range(1, 50_000)]
    print(s)
    plt.plot(s, ',')
    plt.ylabel('some numbers')
    plt.show()

