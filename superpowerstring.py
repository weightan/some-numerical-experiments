from math import prod
from itertools import accumulate
from itertools import chain, combinations, combinations_with_replacement
import random
from random import shuffle
from tqdm import tqdm

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

L = 41
N = 8
populat = list( range(1, N) )
p = [ set(i) for i in powerset( range(1, N) ) if len(i) > 1][::-1]
# p_r = random.sample([])
pairs_set = [list(i) for i in p if len(i) == 2]
#pairs = [shuffle(i) for i in pairs_set ]

def eval_string(st):
    count = 0
    s = []
    for i in p:
        for k in range(L - len(i) + 1):
            if set(st[k: k + len(i)]) == i:
                count += 1
                break
    return count

def is_ideal(st):
    s = []
    for i in p:
        for k in range(L - len(i) + 1):
            c = 0
            if set(st[k: k + len(i)]) == i:
                c = 1
                break
            if c == 0:
                return 0
    print(st, 'hooooray')
    return 1


def eval_covering(st):
    count = 0
    s = []
    for i in p:
        for k in range(L - len(i) + 1):
            if set(st[k: k + len(i)]) == i:
                s.append(1)
                break
        else:
            s.append(0)
    return ''.join(list(map(str, s)))

def generate_string():
    pairs = [i for i in pairs_set ]
    pairs = pairs + pairs
    #print(pairs)
    return random.sample(list(chain.from_iterable(pairs))[:L], L)
    
def random_strings():
    print(len([i for i in p if len(i) == 2]))
    maxc = 0
    maxp = []
    for t in range(10**5):
        st = [ random.choice(populat) for i in range(L)]
        #st = generate_string()

         
        count = eval_string(st)
        if count > maxc:
            print(count, len(p), st)
            print(eval_covering(st))
            maxc = count
            maxp = st

    print(maxc, len(p), maxp)


h = '123456127346257436715236142573142763514765'
h = list(map(int, h))
h2 = [4, 7, 2, 6, 1, 4, 6, 5, 1, 3, 4, 5, 6, 7, 1, 3, 1, 2, 4, 7, 5, 3, 4, 6, 2, 3, 1, 6, 2, 5, 4, 7, 6, 3, 2, 5, 5, 3, 2, 1, 7]
h3 = [1, 2, 4, 7, 1, 6, 5, 2, 1, 4, 3, 7, 6, 4, 2, 7, 3, 5, 1, 7, 2, 3, 4, 5, 7, 3, 4, 5, 6, 7, 5, 2, 5, 3, 6, 4, 2, 6, 1, 6, 1, 3]

if __name__ == "__main__":
    for t in tqdm(range(10**10)):
        L = random.choice([38, 39, 40 ,41])
        st = [ random.choice(populat) for _ in range(L)]
        if is_ideal(st):
            print(st)
            break


    



        