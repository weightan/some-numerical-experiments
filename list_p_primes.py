
import itertools
from tqdm import tqdm
from collections import Counter
# from arrs import *
import math
from sympy import primefactors, sieve
import matplotlib.pyplot as plt

def make_list_of_primes(n):
    primes = []

    for i in range(2, n + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i%j == 0:
                break
        else:
            primes.append(i)

    return primes

def make_list_of_hilbert_primes(n, mod, rem):
    primes = []
    n = (n-rem)//mod

    for i in range(1, n + 1):
        i = mod*i + rem
        for j in range(1, n - 1):
            j = mod*j + rem
            if i % (j) == 0 and i != j:
                
                break

        else:
            primes.append(i)

    return primes

def biggest_comp_num(s):

    
    s_sum = []
    for i in itertools.combinations(s, 2):
        this_number = i[0] * i[1]    # + i[2] * i[3]
        s_sum.append(this_number)

    s_sum = sorted(s_sum)

    m = 0
    mi = 0
    current = 1

    for i in range(1, len(s_sum)):
        
        if s_sum[i - 1] == s_sum[i]:
            curent += 1
            if curent > m:
                m = curent
                mi = s_sum[i]
        else:
            curent = 1

    return (mi, m)# element, counts

def biggest_comp_num_2(s):

    count = 0
    s_sum = []
    for i in tqdm(itertools.combinations(s, 2)):
        this_number = i[0] * i[1] 
        if this_number == 4389:
            count += 1
            print(i)

    return count

def biggest_comp_num_3(s):

    count = 0
    allpars = []

    for i in tqdm(range(1, (406980 + 1) //2 )):

        s_a1 = []
        s_a2 = []

        a = (i, 406980 - i)

        for k in s:
            if k < a[0]:
                if a[0] / k in s and a[0] / k != k:
                    s_a1.append(k, a[0] / k)

            if k < a[1]:
                if a[1] / k in s and a[1] / k != k:
                    s_a2.append(k, a[1] / k)

        for k in range(min(len(s_a1), len(s_a1))):
            pass

            
    return count    

def run_throug_p(mod, rem):
    p = []
    slen = 0
    #for i in range(6000, 120_000):
    for i in range(2, 12_000):

        s = make_list_of_hilbert_primes(i, mod, rem)
        if slen == len(s):
            continue

        slen = len(s)

        char = biggest_comp_num(s)
        print(char, mod, rem)
        #print(f'{char},')
        #p.append(char) 

    #p = sorted(p)
    #print(p)
    # for i in p:
    #     print(i)
    #print(p)


def find_rems_like_hilbert(minn , n):

    m_list = []
    for m in tqdm(range(1, n) ):
        for r in range(1, m):
            if (r*r)%m == r  :  #and r!= 1
                m_list.append((m, r))

    return m_list


def find_rems_like_hilbert_dict(minn = 1 , n = 30_000):

    maxarr = (30030,   [1, 715, 1365, 1716,
                        2080, 2640, 2926, 3081,
                        4005, 4291, 5005, 6006,
                        6370, 6721, 6930, 7371,
                        7645, 8086, 8295, 8646,
                        9010, 10011, 10725, 11011,
                        11935, 12090, 12376, 12936,
                        13300, 13651, 14301, 15015,
                        15016, 15730, 16380, 16731,
                        17095, 17655, 17941, 18096,
                        19020, 19306, 20020, 21021,
                        21385, 21736, 21945, 22386,
                        22660, 23101, 23310, 23661,
                        24025, 25026, 25740, 26026,
                        26950, 27105, 27391, 27951,
                        28315, 28666, 29316])

    maxlen = len(maxarr[1])

    m_dict = {}
    for m in tqdm(range(minn, n)):
        for r in range(1, m) :
            if (r*r)%m == r  :  
                m_dict [m] = m_dict.get(m, [])  + [r]

    
    sieve._reset() 
    sieve.extend_to_no(20)
    primes = sieve._list 

    primes_two = [i[0]*i[1]*i[2]*i[3] for i in itertools.combinations(primes, 4)]


    for k, v in m_dict.items():
        if k in primes_two:
            print(k, v)
            # maxlen = len(v)
            # maxarr = (k, v)

    


    


def find_m_like_hikbert_with_addition(n):

    m_list = []
    for m in range(3, n):
        rem = [k for k in range(m)]
        for r in rem:
            if (r*r)%m == r and (2*r)%m == r and r!= 0 :  #and r!= 1
                m_list.append((m, r))

    return m_list

def check_for_ambigues_primes(num, rem):
    #check primes in a form num*k + rem in terms of this numbers
    list_of_primes = make_list_of_hilbert_primes(10_000, num, rem)

    s_sum = []
    for i in itertools.combinations(list_of_primes, 2):
        this_number = i[0] * i[1]    # + i[2] * i[3]
        s_sum.append((this_number, i) )

    s_sum = sorted(s_sum)

    m = 0
    mi = 0
    current = 1

    for i in range(1, len(s_sum)):
        
        if s_sum[i - 1][0] == s_sum[i][0] :
            curent += 1
            
            if curent > m:
                m = curent
                mi = s_sum[i]
        else:
            curent = 1


    return (num, rem, mi, m)

def check_comb_min(num = 7, rem = 1):
    # num = 8
    # rem = 1

    list_of_primes = make_list_of_hilbert_primes(100, num, rem)

    dict_n = {}

    rems = list(range(1, num +1 ))

    for i, j in itertools.combinations_with_replacement(rems, 2):


        current = (i * j )% num 

        v = dict_n.get(current, [])
        dict_n[current] = v + [(i, j)]

    lis = sorted(dict_n.items(), key = lambda x:x[0])

    for k, v in lis:
        a = []
        for  i in set(v):
            if k not in i and k not in[0] :
                a.append(i)
        dict_n[k] =  a
        print(k, a)

            
    # for k, v in dict_n.items():
    #      set(v)

    return dict_n

def check_all_primes(list_of_rem, num, rem):


    #for i in itertools.combinations():
        pass

from math import prod, factorial
from itertools import product

def factors():
    a = [[1], [2, 3], [4, 4], [2, 2, 4], [3, 3, 4], [2, 2, 2, 2], [3, 3, 3, 3]]
    t = []
    for i in range(len(a)):
        t.append(i * [0])
        for j in range(i, len(a)):
            b = a[i] + a[j]
            b.sort()
            x = 0
            for k in range(len(a)):
                for l in range(k, len(a)):
                    c = a[k] + a[l]
                    c.sort()
                    if b == c:
                        x += prod([factorial(c.count(n)) / (factorial(a[k].count(n)) * factorial(c.count(n) - a[k].count(n))) for n in range(min(c), max(c) + 1)]) / [1, 2][k == l]
            t[-1].append(int(x))

    m = max([len(str(t[i][j])) for i, j in product(range(len(t)), repeat=2)])

    for i in t:
        print("")
        for j in i:
            print(j, (m-len(str(j))) * " ", end="")





def test():
    pass
    # s = make_list_of_hilbert_primes(4389)

    # char = biggest_comp_num_2(s)

    # print('\n', char)

    # run_throug_p()

    #p = find_m_like_hikbert(100)

    # for i in p :
    #     print(i)

    # for i in p:
    #     run_throug_p(i[0], i[1])

    # p = make_list_of_hilbert_primes(10000, 6, 3)
    
    # s = make_list_of_hilbert_primes(40)

    # for i in p:
    #     print(i, (i-3)/6)

    # print(make_list_of_hilbert_primes(100, 4, 1))

from numba import jit


def test_yto_con():

    n_min = 2000

    n_max = 2200

    arr_out = []

    for n in range(n_min, n_max):
        s = list(range(n_min, n))

        for i in itertools.combinations_with_replacement(s, 2):
            if (i[0] * i[1]) % n == 1 and i[0] != i[1] :
                arr_out.append((n, i))
                #print((n, i))

    arr_out = set(arr_out)

    arr_nums = [i[0] for i in arr_out]

    arr_sum = []

    # for n in arr_nums:
    #     for j in arr_out:
    #         if j[0] == n and j[1][0]  < 4 :
    #             arr_sum.append( j)

    # for i in sorted(set(arr_sum)):
    #     print(i)


    for i in range(n_min, n_max):
        if not (i  in arr_nums):
            print (i) 

def ternary (n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))                


import math


def run_b():
    from sympy.ntheory import totient, divisors

    a = [ (sum(n*totient(d)//d  for d in divisors(n)), n) for n in range(1, 100_000)]
    a = sorted(a)[:20_000]

    c = [i[1] for i in a]
    b = [i[0] for i in a]

    #print(c, b)

    # plt.plot(c,   ',')
    # plt.ylabel('some numbers')
    # plt.show()

from itertools import chain, combinations, combinations_with_replacement

def product(lst):
    p = 1
    for i in lst:
        p *= i
    return p

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

ms = [(9_376,), 10_000] 


def find_sets_like_hilbert():
     for i in range(2, 100):
        t = 0

        #print(i)
        for s in powerset(range(1, i)):
            c = 1
            

            for k in combinations_with_replacement(s, 2):
                if (k[0]**2 * k[1]**2)%i not in s:
                    c = 0 
                    break

            if c == 1 and s != () and len(s) > 1 :
                print([s, i], ',')
                t +=1

        #print(t, end=' ')


def find_sets_like_hilbert_oeis():
    from itertools import chain, combinations, combinations_with_replacement
    for i in range(1, 100):
        t = 1
        for s in chain.from_iterable(combinations((list(range(0, i))), r) for r in range(1, i)):
            c = 1
            for k in combinations_with_replacement(s, 2):
                if (k[0]*k[1])%i not in s:
                    c = 0 
                    break
            if c == 1:
                t +=1
        print(t, end=', ')


def check_primes_set():
    out = []
    for i in tqdm(range(100_000_000)):
        if i % ms[1] in ms[0]:
            out.append(i)
            #print(i)

    primes = [] 

    for i in out:

        c = 1
        for j in out:
            if i % j == 0 and i != j and j != 1:
                c  = 0
                #print(i, j)
                break
            if j > i:
                break

        if c == 1:
            primes.append(i)

    out = []
    # for i in powerset(primes):
    #     out.append(product(i))

    for i in combinations(primes, 2):
        out.append(product(i))

    #print(out)

    out = sorted(out)
    cmax = 0
    citem = 0

    for i in range(1, len(out)):
        if out[i] == out[i-1]:
            c += 1
        else:
            if c > cmax:
                cmax = c
                citem = out[i-1]
            c = 0
    print(cmax, citem)

from sympy import prime

def nprime(n, level):
    if level > 1:
        return nprime(prime(n), level - 1)
    else:
        return prime(n)



def pr():
    out = []

    m = 13
    r = 1

    for i in tqdm(range(120_000)):
        if i % m ==  r:
            out.append(i)
            #print(i)

    primes = [] 

    for i in out:

        c = 1
        for j in out:
            if i % j == 0 and i != j and j != 1:
                c  = 0
                #print(i, j)
                break
            if j > i:
                break

        if c == 1:
            primes.append(i)

    return primes

if __name__ == "__main__":
    #find_sets_like_hilbert()
    #find_sets_like_hilbert_oeis()
    #check_primes_set()

    # primes = pr()
    # #print(primes)

    # ways = []

    # for i in tqdm(range(2, max(primes), 13)):
    #     t = 0
    #     for p in primes:
    #         if i - p < 2:
    #             break
    #         if i - p in primes:
    #             t+=1

    #     ways.append(t)

    # import matplotlib.pyplot as plt
    # plt.plot(ways, ',')
    # plt.ylabel('some numbers')
    # plt.show()

    for i in range(1, 20):

        print(nprime(i, i), end = ', ')


