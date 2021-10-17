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


def is_a_hilbert_prime(n):

    if n < 1:
        return 0

    if n == 1 or n == 5:
        return 1

    if n % 4 != 1:
        return 0

    for i in range(5, n, 4):
        if n % i == 0:
            return 0
        if i > n//5:
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
    #10189 15 [1, 0, -1, 0, 10189]

    maxj = 0

    #t = [  i for i in range(0, 50) if i % 4 == 1] + [  -i for i in range(0, 50) if i % 4 == 1] 

    t = [1, 5, 0, 13, -1]

    #random.shuffle(t)


    for p in itertools.product([0,1],t,t,t):

        coef = [*p, 0]

        if p == (0,0,0,0):
            continue

        for  i in range(10**5):

            coef[4] = 4*i + 1
            

            for j in range(500):

                n = 4*j + 1

                ars = coef[::-1]

                f = ars[4]*n**4 + ars[3]*n**3 + ars[2]*n**2 + ars[1]*n + ars[0]

                #f = eval_poly(4*j + 1, coef[::-1])

                if  is_a_hilbert_prime(f) == 0:
                    break


                if j > maxj:
                    print(4*i + 1, j, coef[::-1])
                    maxj = j


def factorial_hil(n):
    s = 1
    for i in range(n, 1, -4):
        if i <= 1:
            break
        s *= i
    return s

if __name__ == "__main__":


    first()


    # c = [8213, 9, 9, 1, 1]
    # c = [733, 89, 57, 1, 1]
    # c = [1697, 13, -17, -1, 1]

    #c =  [22129, -9, 13, -1, 1]

    # c = [772, 0, 1, 0, 0]
    # c = [788, 8, 1, 0, 0]
    # c = [866, 0, 3, 0, 0]

    # c = [788, -8, 1, 0, 0]

    #c = [3092, 4, 1, 0, 0]

    # for i in range(100):
    #     print(i, end = ' ')

    #     i = 4*i + 1

    #     print(i, eval_poly(i, c), is_a_hilbert_prime(eval_poly(i, c)))

    






    


    
