import numpy as np
import itertools
import math
from tqdm import tqdm
import scipy
import functools
import operator

import random
from sympy import *

from itertools import combinations
from itertools import permutations

def forfor(a):
    return [item for sublist in a for item in sublist]

def comd_12():
    dict_n = {}

    arr_out = []

    numbers = list(range(1, 100))

    #print(math.comb(200, 12))

    

    for k in tqdm(range(10_000_000)):

        i = np.random.randint(0, 350, 9)

        a = i[0]**3 + i[1]**3 + i[2]**3

        b = i[3]**3 + i[4]**3 + i[5]**3

        if a != b:
            continue 

        c = i[6]**3 + i[7]**3 + i[8]**3

        if b == c:

            print(a, i)


def comb_cube():
    dict_n = {}

    arr_out = []

    numbers = list(range(1, 250))


    for i in combinations(numbers, 3):
        n = i[0]**3 + i[1]**3 + i[2]**3

        v = dict_n.get(n, 0)

        if   v != 0:

            dict_n[n] = v  + [i]

        elif n > 0:
            dict_n[n] = [i]

    for i, (k, v) in enumerate(dict_n.items()):
        if len(v) >= 3 and len(set(forfor(v))) == len(forfor(v)):

            arr_out.append((k, v, len(v)))

    print('done combinations')

    arr_out = sorted(arr_out, key = lambda x: x[0])

    print('done sort')

    k = 0

    for i in arr_out:
        print (i, ',')

    # dict_of_min_n = {i: (0, 0, 0) for i in range(100)}

    # for i in arr_out:
    #     if dict_of_min_n[i[2]] [0] == 0 or dict_of_min_n[i[2]] [0] > i[0]:
    #         dict_of_min_n[i[2]] =  i

    # for i, (k, v) in enumerate(dict_of_min_n.items()):
    #     if v != (0, 0, 0):
    #         print(v)

def per_cube():
    up_to_n = 1_00_000

    cubes = [i**3 for i in range(1, int(math.pow(up_to_n, 1/3)) + 2)]

    #print(cubes)

    min_dict = {}

    for i in tqdm(range(1, up_to_n)):
        arr_tripl = [i]

        for x in cubes:
            if i - x > 1:
                for y in cubes:
                    if i - x - y > 0:
                        for z in cubes:
                            if  i - x - y - z == 0 and x > y and y > z :
                                arr_tripl.append( (x, y, z) )

        if arr_tripl != [i] and len(set( forfor (arr_tripl[1:]) ))  == len (forfor (arr_tripl[1:]) ):

            k = len(arr_tripl[1:])

            v = min_dict.get(k, 0)

            if v != 0:
                if v[0] > arr_tripl[0]:
                    min_dict[k] = arr_tripl
            else:
                min_dict[k] = arr_tripl

    for i, (k, v) in enumerate(min_dict.items()):
        print(v)


def per_cube_range():
    low_b = 1_00_000 - 1
    up_to_n = 746_992 + 100

    #cubes = [i**3 for i in range(1, int(math.pow(up_to_n, 1/3)) + 2)]

    #print(cubes)

    min_dict = {}

    for i in tqdm(range(1, up_to_n)):
        arr_tripl = [i]

        for x in range(1, int(math.pow(i, 1/3)) + 2 ):
            if i - x**3 > 1:
                for y in range(1, x):
                    for z in range(1, y):
                        if  i - x**3 - y**3 - z**3 == 0 :
                            arr_tripl.append( (x, y, z) )

        if arr_tripl != [i] and len(set( forfor (arr_tripl[1:]) ))  == len (forfor (arr_tripl[1:]) ):

            k = len(arr_tripl[1:])

            v = min_dict.get(k, 0)

            if v != 0:
                if v[0] > arr_tripl[0]:
                    min_dict[k] = arr_tripl
            else:
                min_dict[k] = arr_tripl

    for i, (k, v) in enumerate(min_dict.items()):
        print(v)


def decomp_n(n):
    arr_tripl = []
    arr_cubes  = [i for i in range(1, int(math.pow(n, 1/3)) + 4)]

    for x in arr_cubes:
        if n - x**3 > 1:

            for y in arr_cubes:
                if n - x**3 - y**3 > 0:
                    for z in arr_cubes:
                        if  x>=y and y>= z and n - x**3 - y**3 - z**3 == 0 :
                            arr_tripl.append( (x, y, z) )

    return arr_tripl





if __name__ == "__main__":
    print(decomp_n(5104))




# def forfor(a):
#     return [item for sublist in a for item in sublist]

# up_to_n = 1_000_00

# min_dict = {}

# for i in tqdm(range(1, up_to_n)):
#     arr_tripl = [i]

#     for x in range(1, int(math.pow(i, 1/3)) + 2 ):
#         if i - x**3 > 1:
#             for y in range(1, x):
#                 for z in range(1, y):
#                     if  i - x**3 - y**3 - z**3 == 0 :
#                         arr_tripl.append( (x, y, z) )

#     if arr_tripl != [i] and len(set( forfor (arr_tripl[1:]) ))  == len (forfor (arr_tripl[1:]) ):

#         k = len(arr_tripl[1:])

#         v = min_dict.get(k, 0)

#         if v != 0:
#             if v[0] > arr_tripl[0]:
#                 min_dict[k] = arr_tripl
#         else:
#             min_dict[k] = arr_tripl

#     for i, (k, v) in enumerate(min_dict.items()):
#         print(v)



