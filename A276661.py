from itertools import chain, combinations, combinations_with_replacement, permutations
from random import sample, shuffle
from tqdm import tqdm


def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(1, len(s) ))

def seq_n():
    pass


def seq4(n):
    return 0
    from itertools import combinations

    terms = [0]
    
    sums = set()
    

    for i in range(n):

        t = terms[-1]
    
        while True:
            h = True
            h2 = True

            t += 1

            for j in terms:
                if t + j in sums:
                    h = False
                    break
            if h:
                for j in sums:
                    if t + j in sums:
                        h2 = False
                        break

            if h and h2:
                break 


        terms.append(t)

        for j in powerset(terms):
            sums.add(sum( j ))
        

        print(t, end = ', ')

def check_seq(s):
    sums = set()
    print(len(s))

    for i in chain.from_iterable(combinations(s, r) for r in range(2, len(s) )):
        t = sum(i)
        if t in sums:
            return False
        else:
            sums.add(t)
    print(s, 'hooray')

    return True

def r_search():
    k = 308
    base_set = list(range(1, k + 1 ))
    for i in range(20000):
        
        base_set = sample(base_set, len(base_set))
        s = []
        ind = 0
        sums = set()
        
        for j in range(ind, len(base_set)):

            t = base_set[j]
            h = True

            for k in sums:
                if t+k in sums:
                    h = False
                    break
            if h:
                ind = j+1
                sums.add(t)

                for k in sums.copy():
                    sums.add(k+t)

                #print(sums)
                s.append(t)

        if len(s) >= 8:
            print(s, len(s))











k = 308
base_set = list(range(1, k + 1 ))
restrict = 0
maxs = []
s = set()
sums = set()


def retrac():
    global base_set, s, sums, restrict, maxs
    for i in base_set:
        h = True
        for j in sums:
            if j == i or j+i in sums :
                h = False
                break
        if h:
            base_set.remove(i)
            s.add(i)
            r = sums.copy()

            for g in r:
                sums.add(g+i)

            retrac()

            s.remove(i)
            base_set.append(i)
            sums = r

    if len(s) >= restrict:
        restrict = len(s)
        maxs.append(restrict)
        #print(k, s)

    if len(s) == 0:
        return maxs


for i in tqdm(range(1, 100)):
    k = i
    base_set = list(range(1, k + 1 ))
    restrict = 0
    s = set()
    maxs = []
    sums = set([0])
    g = retrac()

    print(k, max(g))
