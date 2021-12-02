from itertools import chain, combinations, combinations_with_replacement

import random
N = 3
p = [set(i) for i in combinations()]

def generate_supercomb(L):
    s = ''.join(str(random.randint(1, N)) for i in range(L))
    print(s)

def is_a_supercomb(s):



generate_supercomb(10)