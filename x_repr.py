
import numpy as np
import itertools
import math
from tqdm import tqdm
import scipy

import random
from sympy import *



if __name__ == "__main__":


    x, y, z, t = symbols('x y z t')
    k, m, n = symbols('k m n', integer=True)
    f, g, h = symbols('f g h', cls=Function)
    carr = [1,   9,   13,  17,  25,  29,  33,  41,  45,  49,  57,  65,
            73,  77,  81,  89,  93,  97,  105, 109, 113, 121, 129, 137,
            141, 145, 153, 157, 161, 169, 173, 177, 185, 193, 201,
            205, 209, 217, 225, 233, 237, 241, 249, 257, 265, 269,
            273, 281, 285, 289, 297, 301, 305, 313, 321, 329, 333,
            337, 345, 349, 353, 361, 365, 369, 377, 385, 393, 397,
            401, 409, 413, 417, 425, 429, 433, 441, 449, 457, 461,
            465, 473, 481, 489, 493, 497, 505]

    print(len(carr))

    for i in tqdm(range(10**4, 10**10)):
        
        c = i
        r = diophantine(4*(x**2) - 4*y*x*c + 4*(c**2) + (5 - y**3))
        if r != set():
            print(r)
            break