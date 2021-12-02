from math import prod
from itertools import accumulate


def a(n):
    return prod(accumulate(map(int, str(n))))



if __name__ == "__main__":
    #379 
    t = 379
    for i in range(10000):
        t = a(t)
        print(len(str(t)))




