
import itertools
from tqdm import tqdm
from collections import Counter
from arrs import *
import math
from sympy import primefactors, sieve

def rem_like_hilbert(n):
    m_dict = {}
    for m in tqdm(range(1, n)):
        for r in range(1, m) :
            if (r**3)%m == r  and (r**2)%m == r :  
                m_dict [m] = m_dict.get(m, [])  + [r] 


    for i in m_dict.items():
        print(i)




if __name__ == "__main__": 
    rem_like_hilbert(100) 

