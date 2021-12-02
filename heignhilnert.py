import itertools
from tqdm import tqdm
# from collections import Counter
import math
# from sympy import primefactors, sieve
# import matplotlib.pyplot as plt
import random 

# from itertools import chain, combinations, combinations_with_replacement

import numpy as np 
import pickle

m = 7

def pr(m = 4, r = 1):
    out = []
    for i in tqdm(range(400_000)):
        if i % m ==  r:
            out.append(i)

    primes = [] 
    for i in tqdm(out):
        c = 1
        for j in out:
            if i % j == 0 and i != j and j != 1:
                c  = 0
                break
            if j > i:
                break
        if c == 1:
            primes.append(i)

    with open('primeslist', 'wb') as fp:
        pickle.dump(primes, fp)


    return primes, out


def eval_poly(n, signs = [1, 1, 1, 1, 1]):

    return  signs[4]*n**4 + signs[3]*n**3 + signs[2]*n**2 + signs[1]*n + signs[0]


def run():
    #primes, allnumbers = pr()
    primes = []
    with open ('primeslist', 'rb') as fp:
        primes = pickle.load(fp)

    upto = 200

    tmax = 0
    maxprime = max(primes)

    for i in range(1, 30000, 4) :

        #hilbert_gen_polyp = np.poly1d((1, 1, 1, 1, i))
        #print(hilbert_gen_polyp)
        t = 0 

        for n in range(1, 25, 4):
            p = eval_poly(n, i)

            #print((p - 1) % 4)
            if p > maxprime:
                print(p)

            if  p in primes:
                t += 1

        if  t > tmax:
            print(i, t)
            tmax = t
            pmax = i

import functools 
@functools.lru_cache(maxsize= 1_000)
def is_a_hilbert_prime(n):

    if n < 1:
        return 0

    if n == 1 or n == m +1:
        return 1

    if n % m != 1:
        return 0

    for i in range(m+1, n, m):
        if n % i == 0:
            return 0
        if i > n//(m + 1):
            break

    return 1


def run2():
    #run()
    nums = []
    for i in  range(20):
        if i % 4 ==  1:
            nums.append(i)

    nums = nums + [-i for i in nums] + [0]*20

    rtre = [[-5, 13, 17, 9, -9],
            [-13, -17, -1, 0, 0],
            [0, 0, 5, 17, -5],
            [0, -1, 0, -5, -5]
            ]

    for i in range(2000):

        coef = [random.choice(nums) for i in range(5)]

        out = []

        for n in range(1, 50):
            #print(n)
            n = 4*n + 1

            f = eval_poly(n, coef)
            if f % 4 == 1 and f >= 5:
                out.append((f, is_a_hilbert_prime(f)))
            else:
                out.append((f, 0))


        
        t = 0
        for p in  out :
            
            if p[1] == 0:
                break
            else:
                t+=1

        s = sum(j[1] for j in out)

        if s > 0:
            print(coef, s, t)
        else:
            print('--')


def first():
    maxj = 0

    t = [i for i in range(0, 30) ] 

    for p in itertools.product([1],t):

        coef = [0, *p[::-1]]

        #print(coef)

        if p == (0,0):
            continue

        for  i in range(10**5):

            coef[0] = i 

            for j in range(500):

                n = m*j + 1

                f = coef[2]*(n**2) + coef[1]*n + coef[0]

                if  is_a_hilbert_prime(f) == 0:
                    break

                if j > maxj:
                    maxel =  coef
                    maxj = j
                    print(j, maxel)

    return (m, maxel, maxj)


def factorial_hil(n):
    s = 1
    for i in range(n, 1, -4):
        if i <= 1:
            break
        s *= i
    return s

from sympy import isprime


@functools.lru_cache(maxsize= 2000)
def arithmetic_derivative(n):
    if n == 1 or n==0:
        return 0
    if isprime(n):
        return 1

def eval_poly2(n, coef):
    return coef[0] + coef[1]*n + coef[2]*n**2


def first2():

    t1 = [j for j in range(10**3)]
    t2 = [j for j  in range(10**2)]
    t3 = [1]

    for i in range(3, 10):
        m = i
        maxn = 0

        for p in itertools.product(t3, t2, t1):


            if p[1] == 0 and p[2] == 0:
                continue

            p = p[::-1]


            for n in range(1, 500, m):

                

                f = p[0] + p[1]*n + p[2]*n**2

                if  is_a_hilbert_prime(f) == 0:
                    break

                if n > maxn:
                    print(n, p)
                    maxn = n




if __name__ == "__main__":

    #from sympy import isprime
    out = []
    for i in range(3, 14):
        m = i
        t = first()
        print(t)
        out.append(t)

    print(out)


    #first2()


    # c = [8213, 9, 9, 1, 1]
    # c = [19661, 185, 13, 1, 1]
    # c = [22901, 317, 17, 1, 1]
    # c =[23381, 197, 97, 1, 1]#26
    # #c = [3092, 4, 1, 0, 0]

    # с =  [4273, 2716, 1, 1, 0] #mod3 32
    # c = [313, 5, 1, 0, 0] 66
    

    # c = [395, 5, 1, 0, 0] #mod5

    # c = [43421, 7, 1, 0, 0] #mod7

    # # print([i%m for i in c])
    # m = 7

    # for i in range(300):
    #     print(i, end = ' ')

    #     i = m*i + 1

    #     t = eval_poly(i, c)
    #     print(i, t, is_a_hilbert_prime(t), 'isprime - ')

    






    


    
