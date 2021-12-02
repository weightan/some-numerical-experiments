
from tqdm import tqdm

for n in range(10, 12):
    b = 10**n;

    M = set()

    for i in tqdm (range(b)):

        t = i
        L = set()


        while t not in L:
            L.add(t)
            t = (t*t*t)%b

        d = len(L)

        if d not in M:
            M.add(d)

    print(len(M))