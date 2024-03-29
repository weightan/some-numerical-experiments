from tqdm import tqdm

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
    
import numpy as np
import itertools
import math
N =  10**7

cubes = [i**3 for i in range(1, math.floor(math.pow(N, 1/3)) )]
z = np.zeros(N +1, dtype = np.uint8)
for i in itertools.combinations(range(0, len(cubes)), 3):
    m = cubes[i[0]] + cubes[i[1]]+ cubes[i[2]]
    if  m <= N :
        z [m] = z[m]  + 1

arrchek = [1]*50
out = [0]*50

for k, v in enumerate(z):

    if k % 2000 == 0:
        print('-----------------', k)

    if  arrchek[v] == 1 and is_a_term_of_seq(k):
        arrchek[v] = k
        for i in range(1, v + 1):
            if out[i] == 0 and arrchek[i] != 1:
                print(k)
                out[i] = 1
            elif arrchek[i] == 1:
                break
        