import itertools
#from tqdm import tqdm
from collections import Counter

#from arrs import *
import numpy as np
#import random
import math
#import ctypes
from sympy import primefactors, sieve
from sympy.ntheory import qs

from tqdm import tqdm 

sieve._reset() # this line for doctest only
sieve.extend_to_no(40_000)
primes = sieve._list 




def print_strings():
    for i in cycles:
        f =  [format(j , 'b')[::-1] for j in i]
        for j in f:
            print(j)

        print('\n')


def print_strings_div():
    for i in range(len(cycles)):
        temp = []
        for j in range(1, len(cycles[i])):
            dif = cycles[i][j -1] - cycles[i][j ]
            sign = dif/abs(dif)
            bitn = sign*math.log2(abs(dif))

            temp.append(bitn)
        print(temp )

one_c = [19.0, -11.0, 23.0, -19.0, 11.0, -23.0]

def sign(n):
    
    return n/abs(n)




def first_div(n, divis):
    for i in primes:
        if n % i == 0:
            return i == divis
    return False

def first_div_ret(n):
    for i in primes:
        if n % i == 0:
            return i 
    return False


def check_div(n, one_c):
    prew = n
    for one_c in itertools.permutations(one_c):
        for i in range(len(one_c)):
            if first_div(n, abs(one_c[i])):

                n = n - sign(one_c[i])*(2**abs(one_c[i]))

            else:
                continue

        if ( prew == n):
            return True
    
    return False

starts = [85861, 316597, 345439, 518491, 893437, 951121, 1095331, 1326067, 1527961, 1758697]

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

    for i in range(nterms):

        #print(1)
        pf = first_div_ret(current)
        

        if pf  == False:
            break

        s = num_tostr(current, pf + 1)

        
        s = flip_bit(s, pf)

        current = int(s, 2)

        arr = arr + [current]

        if current > 10**3000000:
            break
        if findcycle(arr) != []:
            return arr


    return arr


def run_primes():
    cycl_temp = []
    pa = []
    cr = []
    for i in tqdm(primes[:200]):
        c = flip_seq(i, 10_000)
        cy = findcycle(c)
        cycl_temp = cycl_temp +  [cy]

        cr = cr + [j % 960 for j in cy]

        if len(cy) > 1:
            pa.append((i, len(cy)))
        # if i == 13:
        #     print(cy)

    print(pa)

    print(set(cr))
        

    t = []

    # for i in  cycl_temp:
    #     if i not in t and i != []:
    #         t.append(i) 
             
    # for i in t :
    #     if len(i)> 5:
    #         print(len(i), i) 



def run():

    cycl_temp = []
    pa = []
    cr = []
    #13, 43,115,123,139, 151,159

    for i in [13, 43, 115, 123, 139, 151,159] : #range(3, 400, 2):

        c = flip_seq(i, 10_000)

        cy = findcycle(c)
        print(i, len(c) , len(cy))

        print_arr_as_powers(c)

        if len(cy) >= 7:
            cycl_temp = cycl_temp +  [cy]
            pa.append((i, len(cy)))

    for i in pa:
        print(i)

    t = []

def print_as_powers(n):
    outs = ''

    s = format(n, 'b')
    s = list(s[::-1])


    for i in range( len(s)):

        if s[i] == '1':
            outs = outs + f' + 2**({i})'

    return outs[2:]

def print_arr_as_powers(arr):
    s = ''
    for i in arr:
        s = s  + print_as_powers(i) + ', \n'

    print(s)








def check_div_come():
    one_c = [19.0, -11.0, 23.0, -19.0, 11.0, -23.0]

    for i in range((2**19) + 1, 9978667 + 10):

        n2 = (i - 2**19 )
        n3 = n2 + 2**11
        n4 = n3 - 2**23
        n5 = n4 + 2**19
        n6 = n5 - 2**11
        n7 = n6 + 2**23
        if i % 19 == 0 and n2 % 11 == 0 and  n3 % 23 == 0 and n4 % 19 == 0 and n5 % 11 == 0 and n6 % 23 == 0 and n7 % 19 == 0:
            if i == n7 :
                print(i)

def forfor(a):
    return [item for sublist in a for item in sublist]

def check_rems_in_cycles():

    out_arr = (18, 201894) #8075760 
    s = set(forfor(cycles))

    for n in [8075760]: #tqdm(range(10**6, 10**7)):
        t = []
        for i in s:
            t.append(i%n)

        L = len(set(t))

        if n in  [8075760]: #[3749, 5797, 32591, 34639, 85861
            print(sorted(list(set(sorted(t)))), n, L)
            
        if L / n < out_arr[0]/out_arr[1]:
            out_arr = ( L, n )

    print('done')
    # out_arr = sorted(out_arr, key = lambda x : x[0]/x[1])
    # print(out_arr[])
    print(out_arr)


def findcycle(c):
    t = []
    for i in c:
        if i not in t:
            t.append(i)
        else:
            t.append(i)

            return t[t.index(i):]
    return []



if __name__ == "__main__":
    #run()

    run()

    
    

    #print(a)

    # print(first_div_ret(164_871))
    # c = flip_seq(164_871, 6)
    # print([first_div_ret(i) for i in c])
    # print(c)



    




