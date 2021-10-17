arr = [36, 1009, 12384, 82278, 746992, 5401404,
 15685704, 26936064, 137763072, 251066304, 857520000,
  618817536, 3032856000, 2050677000, 6100691904, 36013192704,
   16405416000, 96569712000, 48805535232, 131243328000] 


import itertools
#from tqdm import tqdm
from collections import Counter

#from arrs import *
import numpy as np
#import random
import math
#import ctypes
from sympy import primefactors, sieve
from sympy.ntheory import qs

from tqdm import tqdm 


if __name__ == "__main__":
 
    for i in range(1,len(arr)):
        d = arr[i-1]  - arr[i] 
        print(d,  arr[i] )
