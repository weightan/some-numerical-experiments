

import numpy as np
import itertools
import math
from tqdm import tqdm
import scipy


from sympy import simplify
from sympy.solvers.diophantine.diophantine import diop_solve
from sympy.solvers.diophantine.diophantine import diop_ternary_quadratic
import random
from sympy.solvers.diophantine.diophantine import diop_quadratic
from sympy import *


def eval_eq_e(e, n):
    out = []
    for x in range(n):
        for y in range(n):
            r = (x**2 + y**2 - e*x*y + x + y)
            if r<0:
                r = r + (abs(r)//n)*(n +2)
            r = r%n
            if (y,x) not in out and r == 0:
                out.append((x,y))
    return set(out)

def forfor(a):
    return [item for sublist in a for item in sublist]

def run():
    x, y, z, t = symbols('x y z t')
    k, m, n = symbols('k m n', integer=True)
    f, g, h = symbols('f g h', cls=Function)

    for e  in [3]:
        out = []
        r = diop_quadratic(x**2 + y**2 - e*x*y + x + y, k )
        for i in r:
            print(i[0], '\n', i[1], '\n')

        for param in tqdm(range(-1, 2)):
            for i in r:
                xout = simplify(i[0].subs(k, param))
                yout  = simplify(i[1].subs(k, param))
                #print(xout, yout)
                if xout > 0 and yout > 0 and (1, yout, xout, e) not in out:
                    out.append( (1, xout, yout, e))


        for j in sorted(out):
            print(*j)

        print(sorted(list(set(forfor(out)))))

        print('\n')

def checkrems():
    for e in range(5, 6):
        print(eval_eq_e(e, 5))

if __name__ == "__main__":
    #checkrems()

    run()