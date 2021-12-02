from tqdm import tqdm
from sympy import factorint, primefactors, divisors
from itertools import chain

def inf_div(n):
    if n == 1: return [1]
    bin_divs, out = {a:format(b, 'b')[::-1] for a, b in factorint(n).items()}, [1]
    for i in divisors(n)[1:-1]:
        c = True
        for p, a in factorint(i).items():
            for k, v in enumerate(format(a, 'b')[::-1]):
                if bin_divs[p][k] == '0' and v != '0':
                    c = False
                    break
        if c: out.append(i)
    return out + [n]

# terms = [6216]
# for i in range(60):
#     terms.append(sum(inf_div(terms[-1]))-terms[-1])
# print(terms)


def a(n):
    return sum(inf_div(n)) 


if __name__ == "__main__":
    #print(list(chain.from_iterable([inf_div(n) for n in range(1, 70)])))
    
    print([n  for n in tqdm(range(1, 600_00) ) if a(n) == 2*n])

    #print([n  for n in tqdm(range(1, 60_000) ) if sum(divisors(n)) == 2*n])