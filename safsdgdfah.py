from tqdm import tqdm

from sympy import primefactors, prod, divisors

def findcycle(c):
    for i in range(2, len(c)//2):
        if c[len(c)-i : ] == c[len(c)-i*2 : len(c)-i]:
            return c[len(c) - i:]
    return []

for K in range(1, 2000):
    terms = [1]

    for i in  range(60_001):
        for j in divisors(terms[-1]):
            if j not in terms:
                terms.append(j)
                break
        else: #prod(primefactors(terms[-1]))
            terms.append(round(terms[-1]*2 )  + K)

        if i in [200, 1000, 2000, 5000, 8000, 10000, 3*10**4, 60_000]:
            s = findcycle(terms)
            if s != []:
                print(K, len(terms), len(s), s  )
                break
    else:
        print(K, None)



    # s = findcycle(terms)

    # if s != []:
    #     print(K, len(terms), len(s)  )
    # else:
    #     print(K, None)


#print(terms)

# print(terms)
