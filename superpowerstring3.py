from itertools import chain, combinations, combinations_with_replacement, permutations
from random import sample, shuffle, random, randint
from tqdm import tqdm


def sum_strings_min(a, b):
    for i in range(len(b), -1, -1):
        if a[len(a) - i:] == b[: i]:
            return a[:len(a)-i] + b
    return a + b

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

record_7 = '45716435724135762415623764523174326172156317' #44
#           71365127162347132546732651426753142753461754
record_8 = '25184321462758136245832618375421864372516843762154681274356847153687253416758132784582681736521347824634675' # 107
r8_2 =     '17568173652317438625184321462758136245832618375421864372516843762154681274356847153687253416745821372846' #104

record_9 = '863245169485714293685196739415762317523681952756354987641375964169835178624591784352341926548739153871897531742846732518672395842695872936785297631548296381748296712896142839762159364275937429187328915461865264138647918423754681237467459618725386493172548931625394726139217'# 273

def concat_powerset(s, powers, maxl):
    if len(s) > maxl:
        return 'a'*(maxl+1)

    if powers == []:
        return s

    if any(''.join(i) in s for i in permutations(powers[-1]) ):
        return concat_powerset(s, powers[:-1], maxl)

    if set(s[- len(powers[-1]) + 1 :]).intersection(powers[-1]) != {}:
        min_s_1 = min((sum_strings_min(s, ''.join(i))       for i in permutations(powers[-1])), key = len)
    else:
        min_s_1 = sum_strings_min(s, ''.join(powers[-1]))

    if set(s[::-1][- len(powers[-1]) + 1 :]).intersection(powers[-1]) != {}:   
        min_s_2 = min((sum_strings_min(s[::-1], ''.join(i)) for i in permutations(powers[-1])), key = len)
    else:
        min_s_2 = sum_strings_min(s[::-1], ''.join(powers[-1]))

    l1 = len(min_s_1)
    l2 = len(min_s_2)

    if l1 > maxl and l2 > maxl:
        return 'a'*(maxl+1)

    if l1 == l2 and min_s_1 != min_s_2 and min_s_1[::-1] != min_s_2 :

        return min(concat_powerset(min_s_1, powers[:-1], maxl),concat_powerset(min_s_2, powers[:-1], maxl), key = len)

    elif abs(l1 - l2) == 1 and random() < 0.01 :
        return min(concat_powerset(min_s_1, powers[:-1], maxl),concat_powerset(min_s_2, powers[:-1], maxl), key = len)

    else:
        return concat_powerset(min(min_s_1, min_s_2, key = len ), powers[:-1], maxl)


wouuu = '163452121314151623241356412356243'

N  = 8
sups = ''
p  = [i for i in powerset(map(str, range(1, N+1))) if len(i) > 1]
p_c = p.copy()

minlen = 44
restriction = minlen

def dfs_solve():
    global minlen 
    global sups
    global p 
    global restriction 

    if len(sups) >= restriction:
        return

    #print(p)
    for term in p:

        perms = [''.join(i) for i in permutations(term)]

        if  any(i in sups for i in perms):
            p.remove(term)

            dfs_solve()

            p.append(term)

            return

        else:
            p.remove(term)

            print(sups, term)
            if set(sups[- len(term) + 1 :]).intersection(p[-1]) != {}:
                min_s_1 = min((sum_strings_min(sups, i) for i in perms), key = len)
            else:
                min_s_1 = sum_strings_min(sups, ''.join(p[-1]))


            if set(sups[::-1][- len(term) + 1 :]).intersection(p[-1]) != {}:
                min_s_2 = min((sum_strings_min(sups[::-1],i) for i in perms), key = len)
            else:
                min_s_2 = sum_strings_min(sups[::-1], ''.join(p[-1]))

            r = sups

            sups = min_s_1

            dfs_solve()

            sups = min_s_2

            dfs_solve()

            sups = r

            p.append(term)

            return

    if minlen >= len(sups):
        minlen = len(sups)
        restriction = minlen
        print(len(sups), sups, is_ok(sups))




def is_ok(st):
    #print(p)
    for i in p_c:
        c = True
        for k in range(len(st) - len(i) + 1):
            if set(st[k:k + len(i)]) == set(i):
                c = False
                break
        if c:
            print(i)
            return False
    #print(st, 'hooooray')
    return True




def is_ok_2(st):
    for term in p_c:
        if not any(''.join(i) in st for i in permutations(term)):
            return False
    return True



def search_for_min_superpowerstring(maxl = 44, N = 8, iters = 10_000):
    p2 = [i for i in powerset(map(str, range(1, N+1))) if len(i) > 1]
    #start = record_7[randint(0, len(record_7)//6) : randint(len(record_7)//6, len(record_7) -1) ]
    sols = ['547136512716234713254673265142675314275346175',
            '71365127162347132546732651426753142753461754',
            '45716435724135762415623764523174326172156317',
            '457136512716234713254673265142675314275346175',
            '123456127346257436715236142573142763514765']

    sols = ['25184321462758136245832618375421864372516843762154681274356847153687253416758132784582681736521347824634675',
            '716248518432675476287431256371862854872318576143527863517486534721864512673486152734681245738162385426318257',
            '82576421362458326183754218643725168437621546812743568471536872534167581327845826817365213478125481342867',
            '8243625187635217348127546285487231857614352786351748653472186451267348615273468124573816238541368247642137652',
            '3125637186285487231857614352786351748653472186451267348615273468124573816238542631246752817342867541832',
            '1325637186285487231857614352786351748653472186451267348615273468124573816238542631246752817342867518432',
            '7684231256371862854872318576143527863517486534721864512673486152734681245738162385426312467528143751483',
            '7682437182576421362458326183754218643725168437621546812743568471536872534167581327845826817365213845481',
            '7682437182576421362458326183754218643725168437621546812743568471536872534167581327845826817365213845184',
            '5841325637186285487231857614352786351748653472186451267348615273468124573816238542631246752817342867',
            '7682437182576421362458326183754218643725168437621546812743568471536872534167581327845826817365213485481']

    sols = ['5841325637186285487231857614352786351748653472186451267348615273468124573816238542631246752817342867']


    record_7 = sample(sols, 1)[0]

    for i in range(iters):
        p2 = [tuple(sample(i, len(i))) for i in p2]
        shuffle(p2)
        #p2 = sorted(p2, key = len)

        #record_8 = r8_2



        if i %  2 == 0:
            record_7 = sample(sols, 1)[0]

            a =  randint(1, len(record_7)//2)
            b = -randint(1, len(record_7)//2)

            start = record_7[ a : b ]

            #print(a, b, start, '---')
            print(i, len(start), maxl, '--')

        s = concat_powerset(start, p2, maxl)
        
        if 'a' not in s and s not in sols and len(s) <= maxl:
            sols.append(s)

            maxl = len(s)
            mins = s
            print(s, len(s))


if __name__ == "__main__":

    dfs_solve()

    #print(is_ok_2('471326543267542186437251684376215468127435684715368725341675813276421357361'))

    # maxl - restriction on the length of the string, only strings with a shorter length will be searched    
    # N - alphabet {1,...,N}
    # iters - number of attempts
    #search_for_min_superpowerstring(maxl = 110, N = 8, iters = 10_000_000)