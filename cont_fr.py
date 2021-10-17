
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


def seq_naiv():
    #a = continued_fraction_reduce([0, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 1, 1, 2, 2])

    a = Fraction(1, 2)
    low_b = 2 + 1

    for t in range(10):

        for i in range(low_b, 4252528 + 1):
            dt = Fraction(1, i)
            currnet_cont_f =  continued_fraction(a + dt)
            c = True

            for j in list(currnet_cont_f):
                if j != 0 and  j != 1 and  j != 2 :
                    c = False
                    break
        
            if c:
                print(i, currnet_cont_f)
                a = a + Fraction(1, i) 
                low_b = i + 1


                break

def seq_naiv_2():
    #a = continued_fraction_reduce([0, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 1, 1, 2, 2])

    a = Fraction(1, 2)
    low_b = 2 + 1

    for t in range(10):

        for i in range(low_b, 4252528 + 1):
            dt = Fraction(1, i)
            currnet_cont_f =  continued_fraction(a + dt)
            c = True

            for j in list(currnet_cont_f):
                if j != 0 and  j != 1 and  j != 2 :
                    c = False
                    break
        
            if c:
                print(i, currnet_cont_f)
                a = a + Fraction(1, i) 
                low_b = i + 1


                break



def dfs_seq(cont_f = [0, 1, 2], ):
    pass



def grad_f():
    stable = [0, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 2]
    offs = random.randrange(-5, 5)

    rs = list(np.random.choice([1,2], 86 - 27 + offs ))
    rs = stable + rs

    fmin = 10**20
    fel = (0, 0)

    oldrs = rs

    for i in tqdm(range(40_000)):
        rs = oldrs.copy()

        x = random.randrange(len(stable), len(rs)  - 1)

        if rs[x] == 1:
            rs[x] = 2
        else:
            rs[x] = 1

        x = random.randrange(len(stable), len(rs)  - 1)

        if rs[x] == 1:
            rs[x] = 2
        else:
            rs[x] = 1

        f = fraction(Fraction(392261117551, 535838651570) - continued_fraction_reduce(rs))

        if abs(fmin) > abs(f[0]):
            fmin = f[0]
            rs = oldrs

    print(fraction(Fraction(392261117551, 535838651570) - continued_fraction_reduce(oldrs)))




def random_g():

    stable = [0, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 2]
    #((1, 958836422851567404099195), 56,            [0, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 2, 2, 1, 1, 2, 1, 2, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2])
    #((1, 955015702623858251895670), 56,            [0, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 2, 2, 1, 1, 2, 1, 2, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 1])
    stable =                                        [0, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 2, 2, 1, 1, 2, 1, 2, 2, 1, 1, 2, 1, 1, 1, 2, 1, 1, 2, 2, 1, 1, 2]
    #((-1, 37802513142351872820305), 42,            [0, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 2, 2, 1, 1, 2, 1, 2, 2, 1, 1, 2, 1, 1, 1, 2, 1])
    #((93, 60139387025071172379486500), 70,         [0, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 2, 2, 1, 1, 2, 1, 2, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 2, 1, 2, 1, 1, 2])
    #((131, 74784815914349091503377424), 59,        [0, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 2, 2, 1, 1, 2, 1, 2, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 2, 1, 2, 2, 1, 2, 1, 1, 1, 1, 1])
    #((-3, 2338611258428813560313890), 46,          [0, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 2, 2, 1, 1, 2, 1, 2, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 2, 2, 1])
    #((-31, 1812724738359207484647505), 57,         [0, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 2, 2, 1, 1, 2, 1, 2, 2, 1, 1, 2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1])
    #((-3, 145606007030120187573650), 56,           [0, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 2, 2, 1, 1, 2, 1, 2, 2, 1, 1, 2, 1, 1, 1, 2, 1, 1, 2, 2, 1, 2, 2, 1, 1, 2, 1, 1, 2, 1, 1])
    #((-27, 1514437217567612278886210), 56,         [0, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 2, 2, 1, 1, 2, 1, 2, 2, 1, 1, 2, 1, 1, 1, 2, 2, 2, 1, 2, 1, 1, 2, 2, 1, 1, 2, 1, 2, 2, 1])
    #((-56761, 2505968911168720202530738745), 72,   [0, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 2, 2, 1, 1, 2, 1, 2, 2, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2
    #((-1, 48556040422372231687230), 51,            [0, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 2, 2, 1, 1, 2, 1, 2, 2, 1, 1, 2, 1, 1, 1, 2, 1, 1, 2, 2, 1, 1, 2, 1, 2, 2])
    fmin = 10**20
    fel =(0,0)
    print( len(stable))
    for i in tqdm(range(100_000)):
        offs = random.randrange(5, 50)
        rs = list(np.random.choice([1,2], offs ))
        rs = stable + rs
        f = fraction(Fraction(392261117551, 535838651570) - continued_fraction_reduce(rs))
        if  f[0] < 0 and  abs(fmin) > abs(f[0]):
            fmin = f[0]
            fel = (f, len(rs), rs)
            print(fmin)
            if f[0] == -1:
                print(f[1])

        if f[0] == -1:
            if f[1] < fel[0][1]:
                print(f[1])
                fel = (f, len(rs), rs)

    print(fel)


            

if __name__ == "__main__":
    #seq_naiv()
    # m = Fraction(1, 2) + Fraction(1,6)+ Fraction(1,18)+Fraction(1,102)+Fraction(1,40936)+Fraction(1,4252528)+Fraction(1,7112715120)
    # print(392261117551/535838651570)

    m02 = continued_fraction(Fraction(1, 2))

    m01 = continued_fraction(Fraction(1, 2) + Fraction(1,6))

    m0 = continued_fraction(Fraction(1, 2) + Fraction(1,6)+ Fraction(1,18))

    m1 = continued_fraction(Fraction(1, 2) + Fraction(1,6)+ Fraction(1,18)+Fraction(1,102))

    m2 = continued_fraction(Fraction(1, 2) + Fraction(1,6)+ Fraction(1,18)+Fraction(1,102)+Fraction(1,40936))

    m3 = continued_fraction(Fraction(1, 2) + Fraction(1,6)+ Fraction(1,18)+Fraction(1,102)+Fraction(1,40936)+Fraction(1,4252528))

    m4 = continued_fraction(Fraction(1, 2) + Fraction(1,6)+ Fraction(1,18)+Fraction(1,102)+Fraction(1,40936)+Fraction(1,4252528)+Fraction(1,7112715120)  +Fraction(1,8778368652367133280 ))

    arr = [m02, m01, m0, m1, m2, m3, m4]

    # for i in range(len(arr)):
    #     print(len(arr[i]))

    print(m4)

    #print( 8778368652367133280 > 48556040422372231687230 > 3.5*10**15 )
    # pretend =[13503318348060140080,
    # 59262741892285687357630,
    # 52158666168169665993550,
    #  62110857985509323630,
    #   75878446598137272010,
    #    5982173961415527127030,
    #     6218976485552727839166,
    #      37802513142351872820305,
    #       43870577823367641068790,
    #        44518615017599244964630,
    #        47422615685425651750830,
    #         109583278271440838686530,
    #         48549304931780594550220,
    #         46894484582715656382160]

    # print(sorted(pretend))

    # for i in pretend:
    #     if i < 8778368652367133280:
    #         print("aaaaaaaaa", i)

    print(m4)
    # print(len(m4)*2)

    stable = [0, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 2]
    # print(len(stable)  )

    # fmin = 10**20
    # fel =(0,0)
    # for i in tqdm(range(40_000)):
    #     offs = random.randrange(-10, 10)
    #     rs = list(np.random.choice([1,2], 86 - 27 + offs ))
    #     rs = stable + rs
    #     f = fraction(Fraction(392261117551, 535838651570) - continued_fraction_reduce(rs))
    #     if abs(fmin) > abs(f[0]):
    #         fmin = f[0]
    #         fel = f
    # print(fel)

    random_g()












    # for i in arr:
    #     print(fraction(continued_fraction_reduce(i)))

    #86

    # for i in range(2, 20):
    #     a.append(i)
    #     print( fraction(continued_fraction_reduce(a)))
 
    

        






    
    # b =  sympify('16/1000', rational=True)
    # print(sympify(Fraction(1, 3) + Fraction(1, 50), rational=True))

    # print(continued_fraction(b))