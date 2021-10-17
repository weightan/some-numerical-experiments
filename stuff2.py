import itertools
from tqdm import tqdm
from collections import Counter
import math
from sympy import primefactors, sieve
import matplotlib.pyplot as plt

from itertools import chain, combinations, combinations_with_replacement


def is_a_term_of_seq(n):
    arr_tripl = []
    for i in range(len(cubes)):
        if n > 1 + cubes[i]:
            for j in range(i):
                for k in range(j):
                    if n  == (cubes[i] + cubes[j] + cubes[k]) :
                        if i in arr_tripl or j in arr_tripl or k in arr_tripl:
                            return False
                        else:
                            arr_tripl = arr_tripl + [i , j , k]
    return arr_tripl != []

#957206 20

def is_a_term_of_seq(n = 3071):
    arr_topl = []
    for p in combinations(list(range(1 , n//4)), 2):
        t  = 4*p[0]*p[1] - p[0] - p[1]
        if t == n:
            arr_topl.append(p)
    print(arr_topl)







def make_arr_4xy():
    a = []
    for p in itertools.permutations(list(range(0 , 1_000)), 2):

        t = p[0]**2 - 4*p[1]
        t2 = p[0]**2 + 4*p[1]

        if t > 0:
            a.append((t, p[0] , -p[1]))

        if t2 > 0:
            a.append((t2, p[0] , p[1]))

    return sorted(a)

def run ():
    a = make_arr_4xy()
    c = 1
    cmax = [0]*500
    s = []
    out = []

    for i in  range(1 , len(a)) :

        if a[i-1][0] == a[i][0]:
            c += 1
            s.append(a[i][1])
            s.append(a[i][2])
        else:
            
            if cmax[c] == 0:
                out.append( (a[i-1][0], c))
                #print(c, a[i-1][0], s, len(set(s)) == len(s))
                cmax[c] = 1

            c = 1
            s = []

    print(sorted(out))

    for i in out:
        print(i[0], end = ", ")

if __name__ == "__main__":
    #is_a_term_of_seq()
    #run()
    print(24 % 16)
    print(24 % 12)

    

    