import itertools
#from tqdm import tqdm

#from arrs import *

#import random
#import math
#import ctypes
from sympy import primefactors, sieve
from sympy.ntheory import qs

from tqdm import tqdm 

from cicl_data import *

arr_of_cicl = [25, 49, 57, 85, 93, 117, 125, 145,
     153, 177, 185, 319, 323, 325, 333, 355,
      357, 363, 365, 385, 393, 407, 417, 425, 437]

c19 = [ 9978667 ,
            3288653 ,
            4557701 ,
            14218441 ,
            6547799 ,
            15631699 ,
            17853863 ,
            21113009 ,
            21286061 ,
            21314903 ,
            23276159 ]

test = [9978667 ,
3288653 ,
4557701 ,
14218441 ,
6547799 ,
15631699 ,
17853863 ,
19820251 ,
21113009 ,
21286061 ,
21314903 ,
23276159 ]

#893871739 [893871739, 894396027, 894396019, 894398067, 894398075, 894398043, 894398035, 894398067]
#12167 [12167, 8400775, 8400807, 8400815, 8400783, 8400775]



def num_tostr(n, length):
    s = format(n, 'b')
    #print(s)
    s = s.zfill(length)
    return s


def flip_bit(s, nbit):
    #nbit -=1
    if len(s) < nbit:
        return s

    s = list(s)[::-1]

    if s[nbit] == '0':
        s[nbit] = '1'
    else:
        s[nbit] = '0'

    return ''.join(s[::-1])


def flip_seq(start, nterms):
    arr = [start]
    current = start

    for i in tqdm(range(nterms)):

        #print(1)
        primes = qs(current, 220, 10_000)
        if primes == set():
            break

        pf = min(primes )
        if pf == 1:
            break

        s = num_tostr(current, pf + 1)

        if pf > 220:
            break
        
        s = flip_bit(s, pf)

        current = int(s, 2)

        arr = arr + [current]

        if current > 2**30:
            break

    return arr


def run():

    # s = num_tostr(13, 10)

    # print(s)

    # s = flip_bit(s, 2)

    # print(s)

    #print(primefactors(8205))
    # cicl = []

    sieve._reset() # this line for doctest only
    sieve.extend_to_no(15_000)
    primes = sieve._list 

    
    #primes = [(31)**i for i in range(2, 7)]
    #primes = [i for i in range(300_001, 400_000, 2)]

    #primes = [19*i  ]

    primes = list(itertools.combinations(primes[10000:], 3))
    primes = [7*i[0] for i in primes]

    #primes = test

    ci_temp = []

    for i in primes:

        arr = flip_seq(i, 20)
        s = []
        for j in range(len(arr)):

            if j < len(arr) and arr[j] in s:
                s.append(arr[j])
                ci_temp = ci_temp + [s]
                print(s, ',')

                break
            
            s.append(arr[j])

            

        #print(i, s)


    # for i in ci_temp:
    #     print(i, ',')



if __name__ == "__main__":

    #print(primefactors(9978667))
    run()

    # sieve._reset() # this line for doctest only
    # sieve.extend_to_no(100)
    # primes = sieve._list 
    # print(primes)

    #31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151


    # t = []

    # for i in cicles:
    #     t.append(i[len(i) - 5:])

    # t2 = []

    # for i in t:
    #     c = i[0]
    #     count = 0

    #     for j in t2:
    #         if c in j:
    #             count += 1
    #             break

    #     if count == 0:
    #         t2.append(i)
        
    # t = t2

    # t = sorted(t, key = lambda x: min(x))
    # for i in t:
    #     print(i, ',')

    # for i in range(10):
    #     print(85 + 1920*i)


    


    # us = [9978667, 9454379, 9456427, 1067819, 1592107, 1590059, 9978667]

    # temp = []

    # for j in us:
    #         print(format(j, 'b'), min(primefactors(j)))
    #         factor = min(primefactors(j))

    #         temp.append(factor)

    # print(temp)




    


    # for i in test:
    #     for j in i:
    #         print(format(j, 'b'), min(primefactors(j)))
    #     print('')






