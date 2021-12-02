# import itertools
from tqdm import tqdm
# from collections import Counter
# from arrs import *
# import math
# import numpy as np
from sympy import primefactors, sieve
# import matplotlib.pyplot as plt
# import plotly.graph_objects as go
import random
import matplotlib.pyplot as plt
# from itertools import chain, combinations, combinations_with_replacement

from sympy import factorint, primefactors

#91 -> [47, 256349, 1898983, 40429703, 1647057173, 889177985724431406826891477659793]

# def prod(lst):
#     r = 1
#     for x in lst:
#         r *= x
#     return r


def a(n, pn = None):
    if n == pn:
        return n
    else:
        p = primefactors(n)
        print(p)
        return a( int("".join([str(i) for i in p])) , n)

def filtern(s):
    s = filter(str.isdigit, list(s))
    s = int("".join(s))
    print(s)
 
import math
def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n // i)
    for divisor in large_divisors[::-1]:
        yield divisor

def divisorGenerator2(n):
    return [i for i in range(1, n) if n%i == 0]



def findcycle(c):
    for i in range(4, len(c)//2):
        if c[len(c)-i : ] == c[len(c)-i*2 : len(c)-i]:
            return c[len(c) - i:]

    return []

# from sympy import primefactors, prod, divisors
# terms = [3]
# for i in range(5000):
#     for j in divisors(terms[-1]):
#         if j not in terms:
#             terms.append(j)
#             break
#     else:
#         terms.append(prod(primefactors(terms[-1]))**2+1)
# print(terms)
# plt.plot(terms, ',')
# plt.ylabel('some numbers')
# plt.show()

def check_seq(k, d = 1):
    terms = [1]
    for i in tqdm(range(10**4)):
        for j in primefactors(terms[-1]):
            if j not in terms:
                terms.append(j)

                break
        else:
            terms.append((terms[-1])*k + d )

        # c = findcycle(terms) 

        # if c != []:
        #     print(c)
            
        #     return 0

    print(terms)
    plt.plot(terms, ',')
    plt.ylabel('some numbers')
    plt.show()
            
    print(None)

from sympy import primefactors, prod, divisors
terms = [1]
for i in tqdm( range(100_000)):
    for j in divisors(terms[-1]):
        if j not in terms:
            terms.append(j)
            break
    else:
        terms.append(prod(primefactors(terms[-1]))*3+1)


# from sympy import primefactors, prod, divisors

def main(n, N):
    for k in range(1, N+1):
       n1=str(n)
       n2 = 1
       for i in range(1, len(n1)+1):
          sum1 = 0
          for j in range(0, i):
             sum1 += int(n1[j])
             n2 = n2*sum1
       if n2 == n:
          return(n)

from math import prod
from itertools import accumulate


def a(n):
    return prod(accumulate(map(int, str(n))))


def eval_s(s):
    return prod(accumulate(s)) 

def make_int(s):
    return int(''.join(map(str, s)))

def step(s, sign):    
    for i in range(random.randint(1, 3)):

        x = random.randint(0, len(s)-1)

        if sign == -1 and s[x] != 0:
            s[x] = s[x] - 1

        if sign == 1 and s[x] != 9:
            s[x] = s[x] + 1
    return s

def step_2(s, sign):
    mind = 10**20
    mins = s

    for x in range(len(s)):
        ds = s.copy()

        if sign == -1 and ds[x] != 0:
            ds[x] = ds[x] - 1

        if sign == 1 and ds[x] != 9:
            ds[x] = ds[x] + 1

        funct = eval_s(s)
        numt = make_int(s)
        dif = funct - numt

        if mind > dif:
            mins = ds

    return mins







def find_eq():
    t = random.randint(10**10, 10**12)
    s = list(map(int, str(t)))

    # print(make_int(s))
    c = 1

    mind = 10**30
    mins = list(map(int, str(mind)))

    for i in tqdm(range(100_000)):

        t = random.randint(10**10, 10**11)
        s = list(map(int, str(t)))

        funct = eval_s(s)
        numt = make_int(s)

        dif = funct - numt

        if abs(dif) < mind:
            mins = s

    s = mins

    funct = eval_s(s)
    numt = make_int(s)
    dif = funct - numt

    print(s, dif)


    for i in tqdm(range(1_00_000)):
        if c == 0:
            break


        for j in range(1_000):

            funct = eval_s(s)
            numt = make_int(s)
            dif = funct - numt

            if funct > numt:
                s = step_2(s, -1)

            if funct < numt:
                s = step_2(s, 1)

            if funct == numt:
                print('hooray!', s)
                c = 0
                break







if __name__ == "__main__":
    print(1)

    t = random.randint(10**10, 10**12)
    s = list(map(int, str(t)))

    funct = eval_s(s)
    numt = make_int(s)

    dif = funct - numt

    print(dif)

    s2 = step_2(s, -1)

    funct = eval_s(s)
    numt = make_int(s)

    dif = funct - numt

    print(s2, dif)

    # find_eq()

    #print([(a(10**i - 1),10**i ) for i in range(12)])

    #56, 45
    # for i in range(2, 100):
    #     for j in range(100):
    #         print(i, j)
    #         check_seq(i, j)

    #check_seq(2, 1)
    # plt.plot(terms, ',')
    # plt.ylabel('some numbers')
    # plt.show()

    



    
