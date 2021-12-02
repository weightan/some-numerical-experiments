

def findcycle(c):
    for i in range(2, len(c)//2):
        if c[len(c)-i : ] == c[len(c)-i*2 : len(c)-i]:
            return c[len(c) - i:]
    return []

def find_cycle2(c):
    for i in range(2, len(c)):
        if c[-i] == c[-1]:
            return i - 1 
    return []

from sympy import nextprime
from tqdm import tqdm



def seq():
    f_map = lambda x, n: (x**2)%n
    terms = []
    t = 1
    for i in tqdm(range(50000)):
        t = nextprime(t)
        L = set()
        n = 10**len(str(t))
        c = t
        while c not in L:
            L.add(c)
            c = f_map(c, n)
        if t == c:
            terms.append(t)

    print(terms)



seq()
