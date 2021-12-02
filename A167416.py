from itertools import permutations
from tqdm import tqdm
from math import factorial
from sympy import sieve, isprime

#A167416 A175429 A177275 A134966

def seq():
    from sympy import sieve, isprime
    from itertools import permutations

    for n in range(1, 20): 
        sieve.extend_to_no(n)
        p = list(map(str, list(sieve._list)))[:n]
        mint = 10**1000
        for i in permutations(p, len(p)):
            t = int(''.join(i))
            if  t < mint and isprime(t):
                mint = t 
        if mint == 10**1000:
            print(-1, end = ', ')
        else:
            print(mint, end = ', ')

def gen_ex(n):
    from sympy import sieve, isprime
    from itertools import permutations

    out = []

    sieve.extend_to_no(n)
    p = list(map(str, list(sieve._list)))[:n]

    for i in permutations(p, len(p)):
        t = int(''.join(i))
        if  isprime(t):
            out.append(t)

    print(len(out)) #, out[:5]


terms = [2, 23, 523, 2357, 112573, 11132357, 1113257317, 111317193257,
         11131719223357, 0, 111317192232935317, 11131719223293157373,
          1113171922329313377541, 111317192232931337415743, 11131719223293133741474357, 0,
           111317192232931337414355975347, 0, '<1113171922329313377595434167615347']

def seq_f():
    out = []
    for n in range(1, 20):
        print(n)
        c = factorial(n)
        #sieve._reset() 
        up_to = n 
        sieve.extend_to_no(up_to)
        p = list(map(str, list(sieve._list)))[:up_to]

        #print(p)

        mint = 10**1000

        f = 0

        for i in permutations(p, len(p)):
            f+=1
            if f % (1 + c//100) == 0:
                print(f//(c//100+1))

            t = int(''.join(i))
            if t < mint and t%2 == 1 and t%3 != 0 and isprime(t):
                mint = t 
                print(t)

        if mint == 10**1000:
            out.append(None)
        else:
            out.append(mint)

        print(out)
        

if __name__ == "__main__":
    print(len(terms))


