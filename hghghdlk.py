from sympy import primefactors, prod, divisors
from itertools import chain, combinations, combinations_with_replacement
from tqdm import tqdm
import random
from math import prod

def a(n):
    return n - sum(map(int, str(n))) - prod(map(int, str(n)))
#print([a(i) for i in range(1, 100)])

from math import prod
from itertools import accumulate
def ok(n):
  return  abs(prod(accumulate(map(int, str(n)[::-1]))) - n)
# print([k for k in range(1, 10**7) if ok(k)])

k = 50

def r():
    for i in range(10**8):
        yield random.randint(10**k, 10**(k + 1))


if __name__ == "__main__":

    minall = 49943941201

    mind = 10**10

    for i in r():
        m = ok(i)
        if  m < mind:
            mind =  m
            print(i,  m)


    # p = [4*i+1 for i in range(1,600) if all(t%4!=1 for t in list(divisors(4*i+1))[1:-1])]

    # print(max([p[i+1] - p[i] for i in range(0, len(p)- 1)]))

    # r = sorted([a*b for a,b in combinations_with_replacement(p, 2)])

    # print([prod(p[:i])  for i in range(1, len(p))])
    # print(p)

    #print(r)




 