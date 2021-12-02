#need several minutes to run

from numpy import zeros, uint8
from itertools import combinations
from math import floor 

N = 10**9
cubes, z = [i**3 for i in range(1, floor(pow(N, 1/3)) )], zeros(N+1, dtype = uint8)
arrcheck, out  = [0] + [1]*50, [True]*50

def is_a_term_of_seq(n):
    seen_c = [False]*len(cubes)
    for i in range(len(cubes)):
        if n > 1 + cubes[i]:
            for j in range(i):
                if n > cubes[i] + cubes[j]:
                    for k in range(j):
                        if n == (cubes[i] + cubes[j] + cubes[k]) :
                            if seen_c[i] or seen_c[j] or seen_c[k]:
                                return False
                            else:
                                seen_c[i] = True;seen_c[j] = True;seen_c[k] = True
    return True

for i in combinations(range(0, len(cubes)), 3):
    m = cubes[i[0]] + cubes[i[1]]+ cubes[i[2]]
    if m <= N:
        z[m] = z[m] + 1

for k, v in enumerate(z):
    if arrcheck[v] == 1 and is_a_term_of_seq(k):
        arrcheck[v] = k
        for i in range(1, v+1):
            if out[i] and arrcheck[i] != 1:
                print(k, end = ', '); out[i] = False
            elif arrcheck[i] == 1:
                break