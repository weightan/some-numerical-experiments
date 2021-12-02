from tqdm import tqdm


def count_overlaps(subs, s):
    c = i = 0
    while i != -1:
        i = s.find(subs, i)
        if i != -1: c += 1; i += 1
    return c

def aupton(terms):
     , astr, numtocount = [0], "0", 0
    for n in tqdm(range(2, terms+1)):
        c = count_overlaps(str(numtocount), astr)
        numtocount = 0 if c == 0 else numtocount + 1
        alst.append(c)
        astr += str(c)
    return alst

terms = aupton(2* 10**5)

import matplotlib.pyplot as plt

plt.plot(terms, ',') #, [i for i in range(len(terms))], 'r--'
plt.ylabel('')
plt.show()

print(terms[-100:])