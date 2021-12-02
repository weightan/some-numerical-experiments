from sympy import factorint, primefactors
from tqdm import tqdm
from math import  factorial
from itertools import count

tail = 514_655_744

def fact_tail(n):
    s = 1

    n2 = 0
    n5 = 0

    for i in range(1, n+1):
        t = i
        while t % 2 == 0:
            n2 +=1 
            t = t//2
        while t % 5 == 0:
            n5 +=1 
            t = t//5

        s = (s*t)%1_000_000_000

    #print(n2, n5)

    if n2 > n5:
        s = (s*(2**(n2- n5)))%1_000_000_000
    if n2 < n5:
        s = (s*(2**(n5- n2)))%1_000_000_000

    return s




if __name__ == "__main__":

    #print(fact_tail( 179472) == tail)
    t = tail

    for i in tqdm(range(179472 +1, 10**9)):
        t = (t*i)%1_000_000_000
        if t== tail:
            print(i)
            break


    #print(str(factorial(179472)))

    # terms = [(179472 , str(factorial(179472)))]

    # for i in range(10):

    #     for j in tqdm(count(terms[-1][0]+1 + 22)):
    #         if terms[-1][1] in str(factorial(j)):
    #             terms.append( (j, str(factorial(j)) )  )
    #             print(j)
    #             break






