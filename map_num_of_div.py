from tqdm import tqdm
from sympy import factorint, primefactors, divisors, divisor_count
from itertools import chain

def findcycle(c):
    for i in range(1, len(c)//2):
        if c[len(c)-i : ] == c[len(c)-i*2 : len(c)-i]:
            return c[len(c) - i:]
    return []

def find_cycle2(c):
    for i in range(2, len(c)):
        if c[-i] == c[-1]:
            return i - 1 
    return 0

H = 10_000
tab = [0]*H
def a(n, x):
    if x < H and tab[x] != 0:
        return n * tab[x]

    elif  x < H :
        tab[x] = divisor_count(x)
        return n * tab[x]
    else:
        return n * divisor_count(x)





def make_seq(n):
    s, t = [1], True
    while t:
        s.append(a(n, s[-1]) )
        for i in range(2, len(s)):
            if s[-i] == s[-1]:
                t = False
                #print(s)
                return( i - 1)
                


def make_seq_2(n):
    s, t = [n], True
    while t:
        s.append(divisor_count(s[-1]) )
        for i in range(2, len(s)):
            if s[-i] == s[-1]:
                t = False
                #print(n, s)
                return( len(s ))
                        

def eval_list(arr):
    return [ make_seq(i) for i in arr] 

def chek_max():
    maxd  = 0
    maxarr = [0 if i >= 19 else -1 for i in range(1, 100) ]
    print(maxarr)

    for i in range(49900000,  10**8):
        if i % 100_000 == 0:
            print(i)
        d = make_seq(i)
        if d > 18 and maxarr[d] == 0:
            maxarr[d] = i
            print(maxarr)
            #print('____________', i, d)


if __name__ == "__main__": 
    chek_max()

    #print ([i*j for i in range(10) for j in range(10)])



    # terms = []
    # for n in range(1, 101):
    #     s = [1]
    #     t = True
    #     while t:
    #         for i in range(2, len(s)):
    #             if s[-i] == s[-1]:
    #                 t = False
    #                 terms.append(find_cycle2(s))
    #                 break
    #         s.append(n * divisor_count(s[-1]))
    # print(terms)
    

