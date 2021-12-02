from tqdm import tqdm
from itertools import accumulate, chain

from sympy import primefactors, prod, divisors, factorint

f = [16, 24, 36, 54, 60, 81, 90, 100, 126, 135, 140, 150, 189, 196, 210, 225, 250, 294, 308, 315, 330, 350, 364, 375, 390, 441, 462, 484, 490, 495, 525, 546, 550, 572, 585, 625, 650, 676, 686, 693, 714, 726, 735, 748, 770, 798, 819, 825, 836, 850, 858, 875, 884, 910, 950, 975, 988]

from itertools import chain
from sympy import factorint
def expand(n):
    return list(chain.from_iterable([[i[0] for j in range(i[1])] for i in factorint(n).items()]))
def is_ok(p,q,r,s):
    return abs(p*q*r - s)<abs(p*s-q*r) 
print([i for  i in range(2, 1000) if len(expand(i)) == 4 and is_ok(*expand(i))]) #~~~~

if __name__ == "__main__":
    pass
    #print([i for  i in range(2, 1000) if len(expand(i)) == 4 and is_ok(*expand(i))])
    #t = factorint(100)
    
    