import itertools
from tqdm import tqdm
from collections import Counter
import math
from sympy import primefactors, sieve
import matplotlib.pyplot as plt
import random 

from itertools import chain, combinations, combinations_with_replacement


# переставка чисел 1.. n с наименшей суммой (s[j-1] ** s[j]) % s[j] длф j = 1..n-1
def evals(arr):
    s = 0

    for j in range(1, len(arr)):
        s += (arr[j-1] ** arr[j]) % arr[j]

    return s

arrm =  [0, 0, 1, 1, 2, 2, 4, 3, 3, 3, 4, 4, 6, 6, 8, 7, 10, 9, 13, 13, 15, 17, 17, 19, 18, 25, 22, 23, 29, 32, 33, 30, 42, 50, 48, 55]
arrm2 = [0, 0, 1, 1, 2, 2, 4, 3, 3, 3, 4, 4, 6, 6, 8, 7, 10, 9, 12, 12, 13, 15, 15, 16, 19, 20, 20, 24, 28, 29, 30, 27, 33, 35, 41, 46, 45, 60  ]
def run ():
    for l in range(2, 40):
        s = list(range(1, l))
        besta = []
        bestscore = 10**10

        for d in range(80_000):

            random.shuffle(s)
            for i in range(10_000):
                count = 0

                for j in range(1, len(s)):

                    #if s[j-1] % s[j] > s[j] % s[j-1]:
                    if (s[j-1] ** s[j]) % s[j] > (s[j] ** s[j-1]) % s[j-1]:

                        t = s[j] 
                        s[j] = s[j-1]
                        s[j-1] = t

                        count += 1

                if count == 0:

                    if evals(s) < bestscore:
                        bestscore = evals(s)
                        besta = s.copy()

                    break
        print(bestscore, end= ', ')

if __name__ == "__main__":

    run()
