
import itertools
from tqdm import tqdm
from collections import Counter
from arrs import *
import math

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
    for i in [40_000]:

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


def find_m_like_hikbert(n):

    m_list = []
    for m in range(5, n):
        rem = [k for k in range(m)]
        for r in rem:
            if (r*r)%m == r and r!= 0 :  #and r!= 1
                m_list.append((m, r))

    return m_list





if __name__ == "__main__":

    # s = make_list_of_hilbert_primes(4389)

    # char = biggest_comp_num_2(s)

    # print('\n', char)

    # run_throug_p()

    p = find_m_like_hikbert(100)

    for i in p:
        run_throug_p(i[0], i[1])

    # p = make_list_of_hilbert_primes(10000, 6, 3)
    
    # s = make_list_of_hilbert_primes(40)

    # for i in p:
    #     print(i, (i-3)/6)
    

    