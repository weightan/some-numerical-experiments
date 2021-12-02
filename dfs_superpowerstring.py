from itertools import chain, combinations, combinations_with_replacement, permutations
from random import sample, shuffle, random, randint

def sum_strings_min(a, b):
    for i in range(len(b), -1, -1):
        if a[len(a) - i:] == b[: i]:
            return a[:len(a)-i] + b
    return a + b

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


N  = 7
sups = '4135762415623764523174326'
p  = [ sample(i, len(i)) for i in powerset(map(str, range(1, N+1))) if len(i) > 1] #tuple(sample(i, len(i))) 
print(p)
p = sample(p, len(p))
#p = sorted(p, key = len)
minlen = 1000
restriction = 1000
p_c = p.copy()

def dfs_solve():
    global minlen 
    global sups
    global p 
    global restriction

    if len(sups) >= restriction:

        return


    for term in p:

        perms = [''.join(i) for i in permutations(term)]

        if any(i in sups for i in perms):
            p.remove(term)

            dfs_solve()

            p.append(term)

            return

        else:
            

            r = sups

            min_s_1 = [sum_strings_min(sups, i) for i in perms]
            

            min_s_2 = [sum_strings_min(sups[::-1], i) for i in perms]
            min_s_1.extend(min_s_2)
            #min_s_1 = sorted(min_s_1, key = len)

            min_s_1_len = min(len(i)for i in min_s_1)

            min_s_1 =  [i for i in min_s_1 if len(i) == min_s_1_len and len(i) < restriction]
            
            print(min_s_1_len)

            p.remove(term)

            for i in min_s_1:
                sups = i
                dfs_solve()

            sups = r

            p.append(term)

            return

    

    if minlen >= len(sups):
        minlen = len(sups)
        restriction = minlen
        print(len(sups), sups, is_ok_2(sups))


def is_ok(st):
    for i in p_c:
        c = True
        for k in range(len(st) - len(i) + 1):
            if set(st[k:k + len(i)]) == set(i):
                c = False
                break
        if c:
            print(i)
            return False
    return True

def is_ok_2(st):
    for term in p_c:
        if not any(''.join(i) in st for i in permutations(term)):
            return False
    return True



if __name__ == "__main__":

    #print(sorted(['11111', '111', '1111'], key = len)[:])

    #print(is_ok_2('312514623456'))

    #print([(is_ok(i), is_ok_2(i)) for i in wouuu])

    dfs_solve()