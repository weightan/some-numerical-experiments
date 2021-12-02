from sympy import factorint, primefactors, divisors, divisor_count
from tqdm import tqdm

c = [   1, 2, 3, 5, 4, 9, 13, 8, 7, 15, 11, 14, 25, 27, 16, 43, 59, 6, 35, 41, 12, 53, 55, 18, 73, 49, 10, 177, 17, 20, 37, 19, 21, 22, 215, 39, 28, 67, 45, 26, 71, 97, 24, 77, 101, 30, 131, 23, 32, 33, 65, 34, 57, 91, 40, 393, 433, 38, 51, 89, 44, 63, 107, 46, 75, 121, 52, 173, 69, 50, 119, 117, 58, 85]
#gcd(terms[-1]+n, t) > 1 and gcd(terms[-1], t) > 1 and gcd(n, t) > 1

from math import gcd
terms, appears = [1, 2], {2:True}
for n in range(3, 100):
    t = 3
    while not(appears.get(t) is None and gcd(terms[-2]+terms[-1], t)>1 and gcd(terms[-2], t)==1 and gcd(terms[-1], t)==1):
        t += 1
    appears[t] = True; terms.append(t);
print(terms)