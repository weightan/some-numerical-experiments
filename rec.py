from tqdm import tqdm
from sympy import sieve, isprime, nextprime

def check_n(n):
    terms = []
    sieve.extend(n)
    pr = sieve._list

    ways = 0

    for start in range(len(pr)):
        if pr[start] > n//2:
            break
        s = 0 

        for i in range(start, len(pr)-1):
            if s > n:
                break
            if s == n and isprime(i - start):
                #print(n, i - start)
                ways +=1
                break

            s += pr[i]
    
    return ways

def sums_arr(n):
    terms = []
    sieve.extend(n+1)
    pr = sieve._list

    ways = []

    for start in range(len(pr)):
        if pr[start] > n//2:
            break
        s = []

        for i in range(start, len(pr)-1):
            if sum(s) > n:
                break
            if sum(s) == n and isprime(i - start):
                #print(n, i - start)
                ways.append(s)
                break

            s.append(pr[i])
    
    return ways

def find_nums():
    terms = [False]*10

    for i in range(5, 10**6):
        if i % 1000 == 0:
            print(i, '----')
        w  = check_n(i)

        if w > 0 and not terms[w] :
            terms[w] = i
            print(terms)

def find_2(n):
    terms = dict()
    sieve.extend(n+1)
    pr = sieve._list

    for start in tqdm(range(len(pr))):

        for i in range(start, len(pr)):
            if isprime(i-start):
                s = sum(pr[start : i])
                if isprime(s):
                    t = terms.get(s)
                    if t is not None:
                        terms[s] += 1
                    else:
                        terms[s] = 1

    terms = sorted(list(terms.items()), key = lambda x : x[0])

    appers = [False]*20

    for  i in terms:
        if not appers[i[1]]:
            appers[i[1]] = i[0] 
            print(appers)




    

is_a_chain = lambda a: all(nextprime(a[i]) == a[i+1] for i in range(len(a)-1))

find_2(100000)





