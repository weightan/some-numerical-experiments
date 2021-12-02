from itertools import chain, combinations, combinations_with_replacement, permutations
from random import sample, shuffle, random


h = '123456127346257436715236142573142763514765' #for N == 7
#h = list(map(int, h))

h_9 = '324812531276483412648314756248153627581362458326183754218643725168437621546812743568471536872534167581327845826817365' # 117
h_8 = '125743261725467132546732651426753142753641756317453' #51

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

N = 9
p = sorted([set(i) for i in powerset(range(1, N)) if len(i) > 1])[::-1]

p2 = [tuple(map(str, i)) for i in powerset(range(1, N)) if len(i) > 1]

print(sorted(p2, key = len))

def is_ok(st):
    for i in p:
        c = True
        for k in range(len(st) - len(i) + 1):
            if set(st[k:k + len(i)]) == i:
                c = False
                break
        if c:
            return False
    print(st, 'hooooray')
    return True

def eval_arr(arr):
    count = 0
    s = []
    for i in p:
        for k in range(len(arr) - len(i) + 1):
            if set(arr[k: k + len(i)]) == i:
                count += 1
                break
    return count

def generate_random_sting(L):

    return random.sample(list(chain.from_iterable(p)), L)

def sum_strings_min(a, b):
    for i in range(len(b), -1, -1):
        if a[len(a) - i:] == b[: i]:
            return a[:len(a)-i] + b
    return a + b

mins = '324812531276483412648314756248153627581362458326183754218643725168437621546812743568471536872534167581327845826817365'
minlen = 117
maxl = minlen

def concat(s, powers):

    if len(s) >= maxl:
        return '0'

    if powers == []:
        #print(neg)
        return s

    if any(''.join(i) in s for i in permutations(powers[-1]) ):
        return concat(s, powers[:-1])

    
    min_s_1 = min((sum_strings_min(s, ''.join(i)) for i in permutations(powers[-1])), key = len)
    min_s_2 = min((sum_strings_min(s[::-1], ''.join(i)) for i in permutations(powers[-1])), key = len)

    l1 = len(min_s_1)
    l2 = len(min_s_2)

    if l1 >= maxl and l2 >= maxl:
        return '0'


    if l1 == l2 and min_s_1 != min_s_2 and min_s_1[::-1] != min_s_2:
        #return min(concat(min_s_1, powers[:-1] ), concat(min_s_2, powers[:-1] ), key = len)

        if random() < 0.5:
            return  concat(min_s_1, powers[:-1])
        else:
            return  concat(min_s_2, powers[:-1])
    else:
        return concat(min(min_s_1, min_s_2, key = len ), powers[:-1])

    #return concat(min(min_s_1, min_s_2, key = len ), powers[:-1])

    #return concat( min(sum_strings_min(s, ''.join(powers[-1])), sum_strings_min(s[::-1], ''.join(powers[-1])), key = len), powers[:-1])

def concat_powerset(s, powers):
    if len(s) >= maxl:
        return '0'

    if powers == []:
        return s

    if any(''.join(i) in s for i in permutations(powers[-1]) ):
        return concat(s, powers[:-1])

    min_s_1 = min((sum_strings_min(s, ''.join(i)) for i in permutations(powers[-1])), key = len)
    min_s_2 = min((sum_strings_min(s[::-1], ''.join(i)) for i in permutations(powers[-1])), key = len)

    l1 = len(min_s_1)
    l2 = len(min_s_2)

    if l1 >= maxl and l2 >= maxl:
        return '0'

    if l1 == l2 and min_s_1 != min_s_2 and min_s_1[::-1] != min_s_2:
        if random() < 0.5:
            return  concat(min_s_1, powers[:-1])
        else:
            return  concat(min_s_2, powers[:-1])
    else:
        return concat(min(min_s_1, min_s_2, key = len ), powers[:-1])


for g in range(1_000_000):

    p2 = [tuple(sample(i, len(i))) for i in p2]
    print(minlen, '--')
    shuffle(p2)
    s = concat('', p2)
    if s != '0' and len(s) < minlen:
        minlen = len(s)
        mins = s
        maxl = minlen

        print(s, len(s))



#print(sum_strings_min('121', '11'))